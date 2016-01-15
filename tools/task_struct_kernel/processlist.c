/* ProcessList.c
Robert Love Chapter 3
*/
#include <linux/kernel.h>
#include <linux/sched.h>
#include <linux/module.h>

int init_module(void)
{
    struct task_struct *task;
    for_each_process(task)
    {
        printk("%s [%d]\n",task->comm , task->pid);
    }

    return 0;
}

void cleanup_module(void)
{
    printk(KERN_INFO "Cleaning Up.\n");
}

