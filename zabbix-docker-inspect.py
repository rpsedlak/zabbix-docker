#!/usr/bin/python

#################################################################
#
# zabbix-docker-inspect.py
#
#   A program that parses the "docker inspect" values for
#   reporting data to Zabbix.
#
# Version: 1.0
#
# Author: Richard Sedlak
#
#################################################################

import sys
import os
import time
import json
import re

#################################################################
# sys.argv[1] - the instanceID of the docker container
# sys.argv[2] - the JSON value of the key to collect
#################################################################

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

    strings = open(file,"r").read()
    return strings

cmd="docker inspect " + sys.argv[1]
strings = local_run_command(cmd,"/tmp/zabbix-docker-inspect-"+sys.argv[1]+".out")

parsed_json = json.loads(strings)

key_path = sys.argv[2].split('.')

ptr = parsed_json[0]

for i in range(0,len(key_path)):
        ptr=ptr[key_path[i]]

# make sure passwords are hidden in zabbix items
if sys.argv[2] == 'Config.Env':
    pwd_pattern = re.compile(r'^(?P<KEY>.*(PASSWORD|PWD).*)=(?P<VALUE>.+)$')
    p_out = []
    for i in ptr:
        match = pwd_pattern.match(i)

        if match:
            p_out.append(match.group('KEY') + "=" + 'x' * len(match.group('VALUE')))
        else:
            p_out.append(i)
    ptr = p_out

print ptr
