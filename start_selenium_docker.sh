#!/usr/bin/env bash

docker stop $(docker ps | grep selenium)

cd ./selepy/
docker-compose up -d
