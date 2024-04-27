wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.7.3-1_amd64.deb && sudo WAZUH_MANAGER='20.124.88.249' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='tpot' dpkg -i ./wazuh-agent_4.7.3-1_amd64.deb


sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
