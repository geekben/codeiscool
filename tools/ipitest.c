//#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/miscdevice.h>
#include <linux/module.h>
#include <linux/smp.h>

#include <asm/uaccess.h>

int times = 10;

/*
* Read the 64-bit TSC (time stamp counter).
*/
static uint64_t rdtsc(void)
{
    unsigned long msw;
    unsigned long lsw;

    __asm__ __volatile__("rdtsc" : "=a" (lsw), "=d" (msw) :);
    return (((uint64_t) msw << 32) | lsw);
}

static void ack_flush(void *_completed)
{
}

static uint64_t send_ipi(void)
{
	int i;
	uint64_t start = rdtsc();
	struct cpumask * mask;
	if (!zalloc_cpumask_var(&mask, GFP_KERNEL))
		return -ENOMEM;
	cpumask_copy(mask, cpu_online_mask);
	cpumask_clear_cpu(num_online_cpus()-1, mask);
	for(i = 0; i < times; i++)
        smp_call_function_many(mask, ack_flush, NULL, 1);
	return rdtsc() - start;

}

static ssize_t ipitest_read(struct file * file, char * buf, 
                          size_t count, loff_t *ppos)
{
        char ret_str[100];
		int len;
		memset(ret_str, 0 ,100);
		sprintf(ret_str, "TSC ticks %lu\n", 
				(unsigned long)send_ipi());
		len = strlen(ret_str);

        if (copy_to_user(buf, ret_str, len+1))
                return -EINVAL;

		if (*ppos != 0)
			return 0;
        /*
         * Tell the user how much data we wrote.
         */
        *ppos = len;

        return len;
}

static ssize_t ipitest_write (struct file * file, const char __user * buf,
                            size_t count, loff_t *ppos)
{
	int len = strlen(buf), ret;
	char *input_str = kmalloc(len+1, GFP_KERNEL);
	if (input_str == NULL)
		return -EINVAL;

	memset(input_str, 0, len+1);
	if (copy_from_user(input_str, buf, len-1))
        return -EINVAL;

	ret = kstrtoint(input_str, 10, &times);

	kfree(input_str);
	if (ret)
		return ret;

	printk("WRITE to ipitest times %d\n", times);
	return len;
}

static const struct file_operations ipitest_fops = {
        .owner                = THIS_MODULE,
        .read                 = ipitest_read,
        .write                = ipitest_write,
};

static struct miscdevice ipitest_dev = {
        /*
         * We don't care what minor number we end up with, so tell the
         * kernel to just pick one.
         */
        MISC_DYNAMIC_MINOR,
        /*
         * Name ourselves /dev/hello.
         */
        "ipitest",
        /*
         * What functions to call when a program performs file
         * operations on the device.
         */
        &ipitest_fops
};

static int __init ipitest_init(void)
{
#if 0
    /*
     * Create an entry in /proc named "hello_world" that calls
     * hello_read_proc() when the file is read.
     */
    if (create_proc_read_entry("hello_world", 0, NULL, hello_read_proc,
                                NULL) == 0) {
            printk(KERN_ERR
                   "Unable to register \"Hello, world!\" proc file\n");
            return -ENOMEM;
    }
#endif
    int ret;

    /*
     * Create the "hello" device in the /sys/class/misc directory.
     * Udev will automatically create the /dev/hello device using
     * the default rules.
     */
    ret = misc_register(&ipitest_dev);
    if (ret)
            printk(KERN_ERR
                   "Unable to register \"tlb flush\" misc device\n");

    return ret;
}

static void __exit ipitest_exit(void)
{
	//remove_proc_entry("hello_world", NULL);
	misc_deregister(&ipitest_dev);
}

module_init(ipitest_init)
module_exit(ipitest_exit)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("luoben");
MODULE_DESCRIPTION("\"IPI\" test module");
MODULE_VERSION("dev");
