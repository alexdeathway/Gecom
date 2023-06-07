#!/bin/bash


git pull origin master

# Stop and remove the current container
sudo docker-compose down

# Build and start production
sudo docker-compose -f docker-compose.prod.yml  up -d --build