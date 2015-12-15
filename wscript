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

def install(ctx):
    ctx.install_as('${PREFIX}/bin/kuku','test.py')
    os.system('chmod +x /usr/local/bin/kuku')
def shutdown(ctx):
    print "shutdown"
