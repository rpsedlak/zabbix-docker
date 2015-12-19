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

#################################################################
# sys.argv[1] - the instanceID of the docker container
# sys.argv[2] - the JSON value of the key to collect
#################################################################

import sys
import subprocess
import json

# sys.argv[1] - container ID
# sys.argv[2] - key value

cmd="docker inspect " + sys.argv[1]
string = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

parsed_json = json.loads(string)

key_path = sys.argv[2].split('.')

ptr = parsed_json[0]

for i in range(0,len(key_path)):
	ptr=ptr[key_path[i]]

print ptr

