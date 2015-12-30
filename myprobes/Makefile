# builds the kprobes example kernel modules;
# then to use one (as root):  insmod <module_name.ko>

obj-m += jprobe.o

default:
	make -C /lib/modules/`uname -r`/build M=`pwd` modules

clean:
	rm -f *.ko* *.mod* *.o .*.cmd modules.order Module.symvers
	rm -rf .tmp_versions
