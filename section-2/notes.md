Troubleschooting - C Docker build Falls (No space on device )

We will determine the disk size df -h docker storage system df du -sh for the current directory docker history <image ID
Temporary solution

docker system prune docker image prune docker container prune docker volume prune

clean apt cache
Solution docker image

Use docker ignore Use smaler base image
For device

Increasing disk capacity Clearing the cache run apt-get update && apt-get install -y nodejs npm && rm -rf/var/lib/apt/list*
