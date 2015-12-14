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

instanceID = sys.argv[1]
keyValue   = sys.argv[2]

print "instanceID: ", instanceID
print "keyValue:   ", keyValue
