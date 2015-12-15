#! /usr/bin/env python

import os
import sys

PPNAME = 'test-project'
VERSION = '1.0.0'

top = '.'
blddir = 'build'

def set_options(opt):
    print "set_options"

def configure(conf):
    conf.load('python')
    print "configure"

def build(bld):
    print "build"
    bld.install_as('${PREFIX}/bin/mulsum','mulsum.py')
    os.system('chmod +x /usr/local/bin/mulsum')

def shutdown(ctx):
    print "shutdown"
