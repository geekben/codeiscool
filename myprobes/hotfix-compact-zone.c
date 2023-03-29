#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kallsyms.h>
#include <linux/cpu.h>
#include <linux/vmalloc.h>

#define RELATIVEJUMP_SIZE   5
#define RELATIVEJUMP_OPCODE 0xe9

unsigned char inst[RELATIVEJUMP_SIZE];

struct mutex *my_text_mutex;

struct compact_control {
        struct list_head freepages;     /* List of free pages to migrate to */
        struct list_head migratepages;  /* List of pages being migrated */
        unsigned long nr_freepages;     /* Number of isolated free pages */
        unsigned long nr_migratepages;  /* Number of pages to migrate */
        unsigned long free_pfn;         /* isolate_freepages search base */
        unsigned long migrate_pfn;      /* isolate_migratepages search base */
        bool sync;                      /* Synchronous migration */
        bool ignore_skip_hint;          /* Scan blocks even if marked skip */
        bool finished_update_free;      /* True when the zone cached pfns are
                                         * no longer being updated
                                         */
        bool finished_update_migrate;

        /* Account for isolated anon and file pages */
        unsigned long nr_anon;
        unsigned long nr_file;

        unsigned int order;             /* order a direct compactor needs */
        int migratetype;                /* MOVABLE, RECLAIMABLE etc */
        struct zone *zone;

        int compact_mode;
        bool contended;
};

static void *(*my_text_poke_smp)(void *addr, const void *opcode, size_t len);
static void *(*my_module_alloc)(unsigned long size);
static void *orig_compact_zone = NULL;
static void *stub_orig_compact_zone = NULL;
static int (*orig_compact_zone_func)(struct zone *zone, struct compact_control *cc);

static int count = 0;

static void * try_to_create_orig_stub(void *orig)
{
        unsigned char *addr = orig;
        unsigned char *stub = NULL;
        int len = 0;
        s32 offset;

        while (len < RELATIVEJUMP_SIZE)
                switch (*addr) {
                case 0x55: /* push %rbp */
                case 0x53: /* push %rbx */
                        addr++;
                        len++;
                        break;
                case 0x48:
                        if (addr[1] == 0x89 && addr[2] == 0xe5) {
                                /* mov    %rsp,%rbp */
                                addr += 3;
                                len += 3;
                        } else if (addr[1] == 0x83 && addr[2] == 0xec) {
                                /* sub    $0xHH,%rsp */
                                addr += 4; /* and an extra offset byte */
                                len += 4;
                        } else if (addr[1] == 0x81 && addr[2] == 0xec) {
                                /* sub    $0xHHHHHHHH, %rsp */
                                addr += 7;
                                len += 7;
                        } else
                                goto out;
                        break;
                case 0x41:
                        switch (addr[1]) {
                        case 0x54 ... 0x57: /* push   %r12/r13/r14/r15 */
                                addr += 2;
                                len += 2;
                                break;
                        default:
                                goto out;
                        }
                        break;
                default:
                        goto out;
        };

        stub = my_module_alloc(PAGE_SIZE);
        if (!stub)
                return NULL;

        memcpy(stub, orig, len);
        offset = (s32)((long)orig + len
                                - ((long)stub + len)
                                - RELATIVEJUMP_SIZE);

        stub[len] = RELATIVEJUMP_OPCODE;
        (*(s32 *)(&stub[len+1])) = offset;
        return (void *)stub;

out:
        {
                int i;

                pr_warning("hotfixes: failed to create orig "
                                "stub, binary are:");
                for (i = 0; i < 16; i++)
                        printk(" %x", *(((unsigned char *)orig)+i));
                printk("\n");
        }
        return NULL;
}

static int overwrite_compact_zone(struct zone *zone, struct compact_control *cc)
{
        printk("compact_zone() fixed\n");
        if (count < 10000 && count++ % 100 == 0)
                pr_warning("count: %d\n", count);
        orig_compact_zone_func = stub_orig_compact_zone;
        return orig_compact_zone_func(zone, cc);
}

static int __init compact_zone_init(void)
{
    unsigned char e9_jmp[RELATIVEJUMP_SIZE];
    s32 offset;

    my_text_poke_smp = (void *)kallsyms_lookup_name("text_poke_smp");
    if (!my_text_poke_smp)
        return -EINVAL;

                pr_warning("compact1\n");
    my_text_mutex = (void *)kallsyms_lookup_name("text_mutex");
    if (!my_text_mutex)
        return -EINVAL;

                pr_warning("compact2\n");
    my_module_alloc = (void *)kallsyms_lookup_name("module_alloc");
    if (!my_module_alloc)
        return -EINVAL;

                pr_warning("compact3\n");
    orig_compact_zone = (void *)kallsyms_lookup_name("compact_zone");
    if (!orig_compact_zone)
        return -EINVAL;

    stub_orig_compact_zone = try_to_create_orig_stub(orig_compact_zone);
    if (!stub_orig_compact_zone)
        return -EINVAL;

                pr_warning("compact4\n");

    offset = (s32)((long)overwrite_compact_zone -
            (long)orig_compact_zone - RELATIVEJUMP_SIZE);

    memcpy(inst, orig_compact_zone, RELATIVEJUMP_SIZE);

    e9_jmp[0] = RELATIVEJUMP_OPCODE;
    (*(s32 *)(&e9_jmp[1])) = offset;

    get_online_cpus();
    mutex_lock(my_text_mutex);
    my_text_poke_smp(orig_compact_zone, e9_jmp, RELATIVEJUMP_SIZE);
    mutex_unlock(my_text_mutex);
    put_online_cpus();

    return 0;
}

static void __exit compact_zone_exit(void)
{
    get_online_cpus();
    mutex_lock(my_text_mutex);
    my_text_poke_smp(orig_compact_zone, inst, RELATIVEJUMP_SIZE);
    mutex_unlock(my_text_mutex);
    put_online_cpus();
    if (stub_orig_compact_zone)
        vfree(stub_orig_compact_zone);
    stub_orig_compact_zone = NULL;

    smp_mb();
}

module_init(compact_zone_init);
module_exit(compact_zone_exit);

MODULE_AUTHOR("Luo Ben <bn0418@gmail.com>");
MODULE_DESCRIPTION("Hotfix for compact_zone");
MODULE_LICENSE("GPL");
MODULE_VERSION("1.0.0");
