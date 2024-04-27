unam -a
Linux tpot 5.10.0-28-cloud-amd64 #1 SMP Debian 5.10.209-2 (2024-01-31) x86_64 GNU/Linux


sudo apt update -y && sudo apt upgrade -y

env bash -c "$(curl -sL https://github.com/telekom-security/tpotce/raw/master/install.sh)"
sudo reboot

firewall setup
64295  - myIP  -  Allow
64297  - myIP  - Allow
1-64200 - anyIP - Allow
