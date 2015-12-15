#!/usr/bin/env pythpn
import argparse
import sys

parser = argparse.ArgumentParser(description=u'test of argparser')
parser.add_argument('-n', type=int, help=u'numnum')
parser.add_argument('x',type=int,help=u'must num1')
parser.add_argument('y',type=int,help=u'must num2')
args = parser.parse_args()

print args.x
print args.y
print args.n
