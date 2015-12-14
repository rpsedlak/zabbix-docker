# zabbix-docker
This repository contains monitoring code for Zabbix to discover and monitor Docker instances on Linux platforms.

This repo is not yet ready for production release.

File(s):
* userparameter_zabbixdocker.conf - Client-side agent parameter definition
* ZabbixDockerTemplate.xml - File to be imported into Zabbix UI for "Template App Docker" template
* zabbix-docker-discover.py - Python script to provide docker instance discovery.
* zabbix-docker-stats.py - Python helper script to provide information from 'docker stats'

NOTE: First integration version


