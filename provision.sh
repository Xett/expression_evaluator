#!/bin/bash

apt-get update
apt-get install -y inotify-tools
apt-get install -y python3-pip
apt-get install -y python3-venv
python3 -m pip install --upgrade build