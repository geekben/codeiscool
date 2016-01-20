obj-m +=processlist.o
obj-m +=traceinit.o
obj-m +=mmdump.o
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean

