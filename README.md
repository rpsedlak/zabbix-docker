# zabbix-docker 1.0.3
This repository contains monitoring code for Zabbix to discover and monitor Docker instances on Linux platforms.

This module once installed provides monitoring capabilities through Zabbix 2.x for Docker version 1.7 and later.

If you experience any software defects related to this module, please notify the author by submitting an issue on [Github](https://github.com/rpsedlak/zabbix-docker/issues).

## Installation Instructions:
* Run package.sh to create the ZabbixDocker.tar.gz file.
* Copy the ZabbixDocker.tar.gz file to necessary servers.
* On the server: tar zxvf ZabbixDocker.tar.gz.  It is recommended that this is done in it's own directory.
* Run install.sh.  Please note that this assumes that the Zabbix agent files are located at /etc/zabbix/zabbix_agentd.d/.  If this is not the case as in an Ubuntu installation then please add the directory as a parameter to install.sh.
* Restart the zabbix-agent process.
* Import the ZabbixDockerTemplate.xml file into Zabbix using the GUI. You can do this from your local computer.

## Files:
* userparameter_zabbixdocker.conf - Client-side agent parameter definition
* ZabbixDockerTemplate.xml - File to be imported into Zabbix UI for "Template App Docker" template
* zabbix-docker-discover.py - Python script to provide docker instance discovery.
* zabbix-docker-stats.py - Python helper script to provide information from 'docker stats'
* zabbix-docker-convert.py - Python helper script to convert byte calculations (i.e. GB -> B)

## Notes:
* Docker 1.7.1 seems to have an issue where it stops responding after so many commands are issued to it.  Several workarounds have been attempted but the long term testing has demonstrated that this is still an issue.  This issue wasn't present in Docker versions 1.8.x (and later).
* Approximately half of the discovered keys for a container that are available are disabled by default.  You may enable these to your taste and needs.  The more data you collect the more storage and processing power you will need.
* The "lifetime" setting for discovered containers is 2 days.  You may vary this based on your needs through the Zabbix UI.  This value only affects the cleanup of containers that are no longer available.

## Testing Information:
* This module was tested using CentOS 6.7, CentOS 7.1, and Ubuntu 14.04 agents and Zabbix server 2.0.16, 2.2.11, and 2.4.7 running on CentOS 6.7.  The Docker versions were 1.7.1 and 1.9.1 used for testing. 

## Disclaimer:
* This code is provided without warranty and responsibility rests completely on the end user for testing, etc.  The author is not responsible for any production issues in any way.
* This code is licensed under [GPLv2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

## Note Bene:
### If you are using this code successfully, please drop me a line at [richard.p.sedlak@gmail.com](mailto:richard.p.sedlak@gmail.com).  I'm just curious if anyone is using it successfully.