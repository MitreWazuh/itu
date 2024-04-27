uname -a

sudo apt update -y && sudo apt upgrade -y

env bash -c "$(curl -sL https://github.com/telekom-security/tpotce/raw/master/install.sh)"
sudo reboot

firewall setup
64295  - myIP  -  Allow
64297  - myIP  - Allow
1-64200 - anyIP - Allow
