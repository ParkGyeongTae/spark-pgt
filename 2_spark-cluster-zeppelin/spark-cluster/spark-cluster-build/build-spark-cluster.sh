#!/bin/bash

IMAGE_NAME=spark-cluster
IMAGE_TAG=0.03

IMAGE_NAME_TAG=$IMAGE_NAME:$IMAGE_TAG

if [[ "$(docker container ls -a --filter="status=exited" -q 2> /dev/null)" != "" ]]; then
    docker rm $(docker container ls -a --filter="status=exited" -q)
fi

if [[ "$(docker images "dangling=true" -q 2> /dev/null)" != "" ]]; then
    echo "Remove dangling images"
    docker rmi $(docker images -f "dangling=true" -q)
fi

if [[ "$(docker container ls -q --filter "name=${CONTAINER_NAME}" 2> /dev/null)" != "" ]]; then
    echo "Stop & Remove Container ${CONTAINER_NAME}"
    docker stop $(docker container ls -q --filter "name=${CONTAINER_NAME}")
    docker rm $(docker container ls -q --filter "name=${CONTAINER_NAME}")
fi

docker build -f ./spark-cluster/spark-cluster-dockerfile/Dockerfile -t $IMAGE_NAME_TAG .