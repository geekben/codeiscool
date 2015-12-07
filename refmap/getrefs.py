# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import re
import os
#import pdfparser as par
import freecite
import MySQLdb as mdb

#Prerequisite: pdfminer installed
#Usage: python <thisfile> <a pdf thesis>
# main
def main(argv):
    #cmd = "pdf2txt.py "+argv[1]+"|sed '0,/^References/ d' > /tmp/refs.txt"
    #os.popen(cmd)
    #par.extractrefs(argv[1],"/tmp/refs.txt")
    cmd = "cd ExtractTxtByPDFbox; java -cp '.:pdfbox-app-2.0.0-RC2.jar' Pdf2txt "+ \
          argv[1]+" > /tmp/refs.txt; cd ../"
    os.popen(cmd)
    with open ("/tmp/refs.txt", "r") as myfile:
        data=myfile.read()

    data = re.sub('^[0-9]+$','',data)
    data = re.sub('-\n','',data)
    data.replace('\n', ' ')
    data = re.sub('\([^\(]*\)','',data)#(xxx)
    data = re.sub('- +','',data)#compu- tor
    #fix the error like ...end.Begin... and excluding the url
    data = re.sub(r'([a-zA-Z0-9]+)\.([A-Z][a-z]*)',r'\1. \2',data)
    #data = re.sub(' +\.','.',data)
    data = re.sub(r'([^ ][^ ]\.) ',r'\1\n',data)

    lines = re.split('\n', data)

    for idx,line in enumerate(lines):
        if re.search('[A-Z][a-z]+, [a-zA-Z]\.',line) or \
           re.search('^\[[0-9]+\] ',line):
            lines[idx] = '\n' + line

    data = ''.join(lines)
    data = re.sub(' +\.','. ',data)
    #fix the error like ...end.Begin... and excluding the url
    data = re.sub(r'([a-zA-Z0-9]+)\.([A-Z][a-z]*)',r'\1. \2',data)
    newlines = data.split('\n')[1:]

    c = freecite.Client()
    citations = c.parse_many(newlines)

    con = mdb.connect('localhost', 'citations', 'citeme', 'citationsdb')
    with con:
        con.set_character_set('utf8')
        cur = con.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        for i in citations:
            authors = ['','','','','']
            for j in range(len(i['authors'])-1):
                authors[j] = i['authors'][j]
            print "insert citations values('',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"% \
                       (i['title'],i['booktitle'],i['journal'],i['volume'],i['pages'],
                        authors[0], authors[1], authors[2], authors[3], authors[4])
            cur.execute("insert citations values(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (i['title'],i['booktitle'],i['journal'],i['volume'],i['pages'],
                        authors[0], authors[1], authors[2], authors[3], authors[4]))


if __name__ == '__main__': sys.exit(main(sys.argv))

