#!/usr/local/python/bin/python

total = 0
free = 0
buffer = 0
cached = 0
huge = 0

with open("/proc/meminfo") as f:
        for line in f:
                temp = line.split()
                if temp[0] == 'MemTotal:':
                        total = int(temp[1])
                if temp[0] == 'MemFree:':
                        free = int(temp[1])
                if temp[0] == 'Buffers:':
                        buffer = int(temp[1])
                if temp[0] == 'Cached:':
                        cached = int(temp[1])
                if temp[0] == 'AnonHugePages:':
                        huge = int(temp[1])

print "%.2f" % (float(huge*100)/(total-free-buffer-cached))
