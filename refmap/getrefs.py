#!/usr/bin/env python

import sys
import re
import os

# main
def main(argv):
    #os.popen("sed '0,/^References/ d' "+argv[1]+" > /tmp/refs.txt")
    with open ("/tmp/refs.txt", "r") as myfile:
            data=myfile.read().replace('\n', ' ')
     
    data = re.sub('\([^\(]*\)','',data)
    data = re.sub('- +','',data)
    lines = re.split('([^ ][^ ]\.) ', data)
    newlines = []
    end = len(lines)
    for i in range(0,end,2):
        if i+1<end: newlines.append(lines[i]+lines[i+1])
        else: newlines.append(lines[i])

    for i,line in enumerate(newlines):
        if re.search(', [a-zA-Z]\. ',line):
            newlines[i] = '\n' + line

    print ''.join(newlines)

if __name__ == '__main__': sys.exit(main(sys.argv))
