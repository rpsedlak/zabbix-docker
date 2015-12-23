#!/usr/bin/python

import sys
import subprocess
import os
import time

errorString="***NOT FOUND***"

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
	return strings

def findString(strings,term):
	found=-1
	ndx=0
	maxNdx=len(strings)
	while (found==-1) and (ndx<maxNdx):
		if term in strings[ndx]:
			found=ndx
		else:
			ndx+=1
	retval=errorString
	if found>=0:
		retval=strings[found]
	return retval
		
def getValue(string):
	pos=string.index(":")
	return string[pos+2:-1]
		

search_for=sys.argv[1]

cmd="docker info"
filename="/tmp/zabbix-docker-info.out"

strings = local_run_command(cmd,filename)

line=findString(strings,search_for)

if errorString in line:
	print search_for, " ", errorString
else:
	print getValue(line)

