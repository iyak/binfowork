#!/usr/bin/env python
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-s','--sum', action='store_const', const=1, help='When you chose sum mode')
parser.add_argument('first_integer',type=int,help='must num1')
parser.add_argument('second_integer',type=int,help='must num2')
args = parser.parse_args()

def add(a,b):
    c = a+b
    return c

def mult(a,b):
    c = a*b
    return c

if __name__ == "__main__":
    x = args.first_integer
    y = args.second_integer
    mode = args.sum
    for i in range(1,x+1):
        print "{0:3d}".format(i),'|',
        for j in range(1,y+1):
            if mode == 1:
                print "{0:3d}".format(add(i,j)),
            else:
                print "{0:3d}".format(mult(i,j)),
        print '\n',

