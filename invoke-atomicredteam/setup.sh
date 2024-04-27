
https://github.com/redcanaryco/invoke-atomicredteam/wiki/Docker-Containers

touch /home/stoksoz/1.csv
chmod 644 /home/stoksoz/1.csv

docker run -it -v /home/stoksoz/1.csv:/1.csv redcanary/invoke-atomicredteam:latest


Test
Invoke-AtomicTest T1003.008
Invoke-AtomicTest All
