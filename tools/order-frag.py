#!/usr/local/python/bin/python
# coding=utf-8

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: %s <order>" % sys.argv[0]
		sys.exit(-1)

	order = int(sys.argv[1])
	if order > 10 or order < 0:
		print "Invalid parameter: order should be 0~10"
		sys.exit(-2)

	info = []
	with open("/proc/buddyinfo") as f:
		for line in f:
			temp = line.split()
			if temp[3] == 'Normal':
				if info == []:
					info = [ int(i) for i in temp[4:] ]
				else:
					for i,v in enumerate(info):
						info[i] += int(temp[4+i])

	free = 0
	ofree = 0
	for i,v in enumerate(info):
		if i >= order:
			ofree = free
		free += v*(4<<i)

	if free == 0:
		print "ERROR: free memory is zero!"
		sys.exit(-3)
	print "%.2f" % (float(ofree) / free * 100)
