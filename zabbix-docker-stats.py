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
import subprocess

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
	'B':B
}	


def pcpu(data):
	pdata=data.split()
	pcpu_data=pdata[1].split('%')[0]
	return pcpu_data

def umem(data):
	pdata=data.split('/')[0].split()
	value = size_options[pdata[3][0]](pdata[2])
	return value

def lmem(data):
	pdata=data.split('/')[1].split()
	value = size_options[pdata[1][0]](pdata[0])
	return value

def pmem(data):
	pdata=data.split()
	pmem_data=pdata[5].split('%')[0]
	return pmem_data

def inet(data):
	pdata=data.split('/')[1].split()
	value = size_options[pdata[4][0]](pdata[3])
	return value

def onet(data):
	pdata=data.split('/')[2].split()
	value = size_options[pdata[1][0]](pdata[0])
	return value

options = {
	'pcpu':pcpu,
	'umem':umem,
	'lmem':lmem,
	'pmem':pmem,
	'inet':inet,
	'onet':onet
}

container=sys.argv[1]
key=sys.argv[2]

cmd="docker stats --no-stream=true " + container
strings = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readlines()

print options[key](strings[1])

