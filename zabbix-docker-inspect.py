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
import subprocess
import os
import time
import json

#################################################################
# sys.argv[1] - the instanceID of the docker container
# sys.argv[2] - the JSON value of the key to collect
#################################################################


def local_run_command(cmd,file):
	cmd = cmd + " | tee > " + file 
	if os.path.isfile(file):
		(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
		ticks=int(time.time())
		delta=ticks-mtime
		if (delta > 60):
			os.system(cmd)
		else:
	else:
		os.system(cmd)

	strings = open(file,"r").readlines()
	return strings

# sys.argv[1] - container ID
# sys.argv[2] - key value

cmd="docker inspect " + sys.argv[1]
string = local_run_command(cmd,"/tmp/zabbix-docker-inspect-"+sys.argv[1]+".out")[0]
#string = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

parsed_json = json.loads(string)

key_path = sys.argv[2].split('.')

ptr = parsed_json[0]

for i in range(0,len(key_path)):
	ptr=ptr[key_path[i]]

print ptr

