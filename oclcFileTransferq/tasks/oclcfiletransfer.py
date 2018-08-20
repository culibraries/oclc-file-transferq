#!/usr/bin/env python

import sys

def transferfile(filename):
    return "PDF({0}) successfully uploaded to OCLC".format(filename)

if __name__ == '__main__':
    filename='example.pdf' #set default
    if len(sys.argv)>1:
        filename= sys.argv[1]
    print(transferfile(filename))
