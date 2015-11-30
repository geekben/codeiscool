#!/usr/bin/env python

import sys
import re
import os
import pdfparser as par
import freecite

#Prerequisite: pdfminer installed
#Usage: python <thisfile> <a pdf thesis>
# main
def main(argv):
    #cmd = "pdf2txt.py "+argv[1]+"|sed '0,/^References/ d' > /tmp/refs.txt"
    #os.popen(cmd)
    par.extractrefs(argv[1],"/tmp/refs.txt")
    with open ("/tmp/refs.txt", "r") as myfile:
        data=myfile.read()
     
    data = re.sub('^[0-9]+$','',data)
    data = re.sub('-\n','',data)
    data.replace('\n', ' ')
    data = re.sub('\([^\(]*\)','',data)#(xxx)
    data = re.sub('- +','',data)#compu- tor
    #fix the error like ...end.Begin... and excluding the url
    data = re.sub(r'([a-zA-Z]+)\.([A-Z][a-z]*)',r'\1. \2',data)
    #data = re.sub(' +\.','.',data)
    data = re.sub(r'([^ ][^ ]\.) ',r'\1\n',data)

    lines = re.split('\n', data)

    for i,line in enumerate(lines):
        if re.search('[A-Z][a-z]+, [a-zA-Z]\.',line) or \
           re.search('^\[[0-9]+\] ',line):
            lines[i] = '\n' + line

    data = ''.join(lines)
    data = re.sub(' +\.','. ',data)
    #fix the error like ...end.Begin... and excluding the url
    data = re.sub(r'([a-zA-Z]+)\.([A-Z][a-z]*)',r'\1. \2',data)
    newlines = data.split('\n')[1:]

    c = freecite.Client()
    citations = c.parse_many(newlines)
    print citations

if __name__ == '__main__': sys.exit(main(sys.argv))
