/* mmdump.c
Ben Luo
*/
#include <linux/kernel.h>
#include <linux/sched.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <asm/pgtable.h>

static int pid = -1;
module_param(pid, int, S_IRUGO);

static int bad_address(void *p)
{
    unsigned long dummy;

    return probe_kernel_address((unsigned long *)p, dummy);
}

static void dump_pagetable(unsigned long address, pgd_t * pgd)
{
    pud_t *pud;
    pmd_t *pmd;
    pte_t *pte;

    if (bad_address(pgd))
        goto bad;

    //printk("PGD %lx ", pgd_val(*pgd));

    if (!pgd_present(*pgd))
        goto out;

    pud = pud_offset(pgd, address);
    if (bad_address(pud))
        goto bad;

    printk("PUD %lx ", pud_val(*pud));
    if (!pud_present(*pud) || pud_large(*pud))
        goto out;

    pmd = pmd_offset(pud, address);
    if (bad_address(pmd))
        goto bad;

    printk("PMD %lx ", pmd_val(*pmd));
    if (!pmd_present(*pmd) || pmd_large(*pmd))
        goto out;

    pte = pte_offset_kernel(pmd, address);
    if (bad_address(pte))
        goto bad;

    printk("PTE %lx", pte_val(*pte));
out:
    printk("\n");
    return;
bad:
    printk("BAD\n");
}

void mmdump(struct mm_struct *mm)
{
    struct vm_area_struct * vma = mm->mmap;
    while(vma) {
        //if(vma->vm_flags)
        if (vma->vm_file){
            printk(KERN_INFO "%lx %lx %s\n", 
                    vma->vm_start, vma->vm_end, vma->vm_file->f_path.dentry->d_iname);
        }
        else{
            unsigned long addr = vma->vm_start;
            printk(KERN_INFO "%lx %lx [anon]\n", 
                    vma->vm_start, vma->vm_end);
            printk(KERN_INFO "---------------start------------------\n");
            for (;addr < vma->vm_end; addr += PAGE_SIZE) 
                dump_pagetable(addr, mm->pgd);
            printk(KERN_INFO "----------------end---------------\n");
        }

        vma = vma->vm_next;
    }
}

int init_module(void)
{
    struct task_struct *task;
    for_each_process(task)
    {
        if (pid == -1)
            printk("echo a pid to me");

        if (task->pid == pid)
            mmdump(task->mm);
    }

    return 0;
}

void cleanup_module(void)
{
    printk(KERN_INFO "Cleaning Up.\n");
}

