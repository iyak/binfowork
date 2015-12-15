#!/usr/bin/env python
import argparse
import sys

#parser = argparse.ArgumentParser()
#parser.add_argument('--foo', help='foo help')
#args = parser.parse_args()
if len(sys.argv) <= 2:
    print >> sys.stderr,"Useage: test <integer> <integer>"
    sys.exit

def add(a,b):
    c = a+b
    return c

def mult(a,b):
    c = a*b
    return c

if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    if len(sys.argv) == 4:
        opt = sys.argv[3]
    else:
        opt = 'default'
    for i in range(1,x+1):
        print "{0:3d}".format(i),'|',
        for j in range(1,y+1):
            if opt == 'default':
                print "{0:3d}".format(mult(i,j)),
            elif opt == '-a':
                print "{0:3d}".format(add(i,j)),
        print '\n',

