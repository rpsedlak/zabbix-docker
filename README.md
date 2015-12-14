# zabbix-docker 0.1.1
This repository contains monitoring code for Zabbix to discover and monitor Docker instances on Linux platforms.

This repo is not yet ready for production release.

File(s):
* userparameter_zabbixdocker.conf - Client-side agent parameter definition
* ZabbixDockerTemplate.xml - File to be imported into Zabbix UI for "Template App Docker" template
* zabbix-docker-discover.py - Python script to provide docker instance discovery.
* zabbix-docker-stats.py - Python helper script to provide information from 'docker stats'
* zabbix-docker-convert.py - Python helper script to convert byte calculations (i.e. GB -> B)

Installation Instructions
* Run package.sh to create the ZabbixDocker.tar.gz file.
* Copy the ZabbixDocker.tar.gz file to necessary servers.
* On the server: tar zxvf ZabbixDocker.tar.gz.  It is recommended that this is done in it's own directory.
* Restart the zabbix-agent process.
* Import the ZabbixDockerTemplate.xml file into Zabbix using the GUI.
* Please note that if you are running a previous version of this monitoring component then you may have to completely remove the template before reinstalling it.

Testing Information:
* This module was tested using CentOS 6.7 and Zabbix 2.0.x.

