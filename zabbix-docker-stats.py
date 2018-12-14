#!/usr/bin/python

#################################################################
#
# zabbix-docker-stats.py
#
#   A program that produces information for Zabbix to
#   process Docker container statistics.
#
# Version: 1.0
#
# Author: Richard Sedlak
#
#################################################################

import sys
import os
import time
import re

def B(b):
    return int(float(b))

def KB(b):
    return int(float(b) * 1024)

def MB(b):
    return int(float(b) * 1024 * 1024)

def GB(b):
    return int(float(b) * 1024 * 1024 * 1024)

def TB(b):
    return int(float(b) * 1024 * 1024 * 1024 * 1024)

def PCT(b):
    return int(b)

size_options = {
    'k':KB,
    'K':KB,
    'm':MB,
    'M':MB,
    'g':GB,
    'G':GB,
    't':TB,
    'T':TB,
    'b':B,
    'B':B,
    '%':PCT
}

def recalc(data):
     pat = re.compile(r'([0-9.]+)([a-zA-Z%])')
     mo = pat.match(data)
     if mo:
         number, unit = mo.group(1,2)
         value = size_options[unit](number)
     else:
         value = False
     return value

def pcpu(data):
     return recalc(data[2])

def umem(data):
     return recalc(data[3])

def lmem(data):
     return recalc(data[5])

def pmem(data):
     return recalc(data[6])

def inet(data):
     return recalc(data[7])

def onet(data):
     return recalc(data[9])

options = {
    'pcpu':pcpu,
    'umem':umem,
    'lmem':lmem,
    'pmem':pmem,
    'inet':inet,
    'onet':onet
}

def local_run_command(cmd,file):
    cmd = cmd + " | tee > " + file
    if os.path.isfile(file) == False:
        os.system(cmd)
    else:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
        ticks=int(time.time())
        delta=ticks-mtime
        if (delta > 60):
            os.system(cmd)

    strings = open(file,"r").readlines()
    return strings[1].split()


container=sys.argv[1]
key=sys.argv[2]

cmd="docker stats --no-stream=true " + container
strings = local_run_command(cmd,"/tmp/zabbix-docker-stats-"+container+".out")

print options[key](strings)
