#!/usr/bin/env bash

docker stop $(docker ps | grep selenium) || true

cd ..
docker-compose up -d
