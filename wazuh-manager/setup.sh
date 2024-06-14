uname -a

Standard D2s v3 (2 vcpus, 8 GiB memory)
Source image publisher :canonical
Source image offer : 0001-com-ubuntu-server-jammy
Source image plan: 22_04-lts-gen2


curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a


FW setup
/////////////////////////////
443  anyIp  Allow
1514  anyIp  Allow  
1515  anyIp  Allow
514  anyIp Allow
