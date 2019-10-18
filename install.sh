#!/bin/bash

# argument processing
if [ -d "/etc/zabbix/zabbix_agentd.d/"  ];
        then CONFIG_PATH=/etc/zabbix/zabbix_agentd.d/

elif [ -d "/etc/zabbix/zabbix_agentd.conf.d/"  ];
        then CONFIG_PATH=/etc/zabbix/zabbix_agentd.d.conf.d/

else
  echo "Zabbix Config Path not found - please enter path:"
  read -r CONFIG_PATH

fi

# Copy the files
cp -f *.py /usr/local/bin
cp -f *.conf $CONFIG_PATH
cp -f *.xml /tmp

# tell the user some stuff
echo "Python scripts copied to /usr/local/bin"
echo "zabbix-agent configuration files copied to $CONFIG_PATH"
echo "XML Zabbix Templates copied to /tmp"
echo ""
echo "You will need to restart the zabbix-agent and import the XML template on your Zabbix server"
