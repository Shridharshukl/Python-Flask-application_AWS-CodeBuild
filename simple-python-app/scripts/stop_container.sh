#!/bin/bash

set -e

echo " docker container is stop and removed "

docker stop demoapp && docker rm demoapp

echo " success -> rm"