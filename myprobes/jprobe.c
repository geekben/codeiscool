/*
 * Here's a sample kernel module showing the use of jprobes to dump
 * the arguments of do_fork().
 *
 * For more information on theory of operation of jprobes, see
 * Documentation/kprobes.txt
 *
 * Build and insert the kernel module as done in the kprobe example.
 * You will see the trace data in /var/log/messages and on the
 * console whenever do_fork() is invoked to create a new process.
 * (Some messages may be suppressed if syslogd is configured to
 * eliminate duplicate messages.)
 */

#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/kprobes.h>

/*
 * Jumper probe for do_fork.
 * Mirror principle enables access to arguments of the probed routine
 * from the probe handler.
 */

/* Proxy routine having the same arguments as actual do_fork() routine */
static long jnative_send_call_func_ipi(const struct cpumask *mask)
{
    char buf[128];
    
    memset(buf, 0,128);
    cpumask_scnprintf(buf,128, mask);
	printk(KERN_INFO "[myprobe][native_send_call_func_ipi]: %s\n", buf);

    dump_stack();

	/* Always end with a call to jprobe_return(). */
	jprobe_return();
	return 0;
}

static long jflush_tlb_page(struct vm_area_struct *vma,
                          unsigned long addr)
{
	printk(KERN_INFO "[myprobe][flush_tlb_page]: %lx\n", addr);

    dump_stack();

	/* Always end with a call to jprobe_return(). */
	jprobe_return();
	return 0;
}

static long jflush_tlb_others(const struct cpumask *cpumask,
                    struct mm_struct *mm,
                    unsigned long start,
                    unsigned long end)
{
	printk(KERN_INFO "[myprobe][flush_tlb_others]");

    dump_stack();

	/* Always end with a call to jprobe_return(). */
	jprobe_return();
	return 0;
}

static struct jprobe my_jprobe1 = {
	.entry			= jnative_send_call_func_ipi,
	.kp = {
		.symbol_name	= "native_send_call_func_ipi",
	},
};

static struct jprobe my_jprobe2 = {
	.entry			= jflush_tlb_page,
	.kp = {
		.symbol_name	= "flush_tlb_page",
	},
};

static struct jprobe my_jprobe3 = {
	.entry			= jflush_tlb_others,
	.kp = {
		.symbol_name	= "flush_tlb_others",
	},
};

static int __init jprobe_init(void)
{
	int ret;

	ret = register_jprobe(&my_jprobe1);
	if (ret < 0) {
		printk(KERN_INFO "register_jprobe1 failed, returned %d\n", ret);
		return -1;
	}
	printk(KERN_INFO "Planted jprobe at %p, handler addr %p\n",
	       my_jprobe1.kp.addr, my_jprobe1.entry);

	ret = register_jprobe(&my_jprobe2);
	if (ret < 0) {
		printk(KERN_INFO "register_jprobe2 failed, returned %d\n", ret);
		return -1;
	}
	printk(KERN_INFO "Planted jprobe at %p, handler addr %p\n",
	       my_jprobe2.kp.addr, my_jprobe2.entry);

	ret = register_jprobe(&my_jprobe3);
	if (ret < 0) {
		printk(KERN_INFO "register_jprobe3 failed, returned %d\n", ret);
		return -1;
	}
	printk(KERN_INFO "Planted jprobe at %p, handler addr %p\n",
	       my_jprobe3.kp.addr, my_jprobe3.entry);

	return 0;
}

static void __exit jprobe_exit(void)
{
	unregister_jprobe(&my_jprobe1);
	printk(KERN_INFO "jprobe at %p unregistered\n", my_jprobe1.kp.addr);
	unregister_jprobe(&my_jprobe2);
	printk(KERN_INFO "jprobe at %p unregistered\n", my_jprobe2.kp.addr);
	unregister_jprobe(&my_jprobe3);
	printk(KERN_INFO "jprobe at %p unregistered\n", my_jprobe3.kp.addr);
}

module_init(jprobe_init)
module_exit(jprobe_exit)
MODULE_LICENSE("GPL");
