//https://github.com/redcanaryco/invoke-atomicredteam/wiki/Docker-Containers


git clone https://github.com/redcanaryco/invoke-atomicredteam.git
cd invoke-atomicredteam/docker
# edit Dockerfile
docker build -t invoke-atomicredteam:latest .
docker run -it invoke-atomicredteam:latest


Test
Invoke-AtomicTest T1003.008
