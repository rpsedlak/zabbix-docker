# Release notes

## Release 1.0.3 - 12/22/2015
* #28 - Fixed 'Running instances showing OOMKilled set to true'
* #27 - Fixed 'ID from 'docker info' only returning a partial value'
* #15 - Fixed 'Requests for data appears to be overloading 'docker' command'

## Release 1.0.2 - 12/21/2015
* #24 - Fixed container memory % report for Ubuntu
* #23 - Fixed false "down" report for Ubuntu

## Release 1.0.1 - 12/21/2015
* #20 - Changed collection delay for docker version
* #18 - Implemented WARNING trigger for paused containers
* #17 - Implemented AVERAGE trigger for OMMKilled containers
* #16 - Corrected install.sh problem for overridden directories
* #15 - Implemented value file caching on zabbix-agent host to keep docker from becoming over loaded.
* #12 - Changed "Docker Storage Driver Deferred Removal Enabled" from text to unsigned int (Boolean value).

## Release 1.0.0 - 12/19/2015
* Feature complete
* Supports docker 'inspect'
* Supports docker 'stats' commands
* Supports docker 'info'
* Supports Zabbix LLD

