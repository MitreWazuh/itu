uname -a
Linux tpot2 5.10.0-28-cloud-amd64 #1 SMP Debian 5.10.209-2 (2024-01-31) x86_64 GNU/Linux



lshw -short
WARNING: you should run this program as super-user.
H/W path      Device      Class      Description
================================================
                          system     Computer
/0                        bus        Motherboard
/0/0                      memory     1GiB System memory
/0/1                      processor  Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz
/0/2                      system     PnP device PNP0b00
/0/3          scsi0       storage    
/0/3/0.0.2    /dev/cdrom  disk       Virtual DVD-ROM
/0/3/0.0.2/0  /dev/cdrom  disk       
/1            eth0        network    Ethernet interface
WARNING: output may be incomplete or inaccurate, you should run this program as super-user.



sudo apt update -y && sudo apt upgrade -y
sudo apt install git
sudo git clone https://github.com/telekom-security/tpotce
cd tpotce/
./install.sh –type=user
