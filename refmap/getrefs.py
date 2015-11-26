#!/usr/bin/env python

import sys
import re
import os

#Prerequisite: pdfminer installed
#Usage: python <thisfile> <a pdf thesis>
# main
def main(argv):
    cmd = "pdf2txt.py "+argv[1]+"|sed '0,/^References/ d' > /tmp/refs.txt"
    os.popen(cmd)
    with open ("/tmp/refs.txt", "r") as myfile:
        data=myfile.read()
        data = re.sub('^[0-9]+$','',data)
        data.replace('\n', ' ')
     
    data = re.sub('\([^\(]*\)','',data)#(xxx)
    data = re.sub('- +','',data)#compu- tor
    #fix the error like ...end.Begin... and excluding the url
    data = re.sub(r'([a-zA-Z]+)\.([A-Z][a-z]*)',r'\1. \2',data)
    #data = re.sub(' +\.','.',data)
    data = re.sub(r'([^ ][^ ]\.) ',r'\1\n',data)

    lines = re.split('\n', data)

    for i,line in enumerate(lines):
        if re.search('[A-Z][a-z]+, [a-zA-Z]\.',line):
            lines[i] = '\n' + line

    print ''.join(lines)

if __name__ == '__main__': sys.exit(main(sys.argv))
