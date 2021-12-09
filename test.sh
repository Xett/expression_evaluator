#!/bin/bash
cd /vagrant

echo "Installing"
python3 -m pip install /vagrant

echo "Testing"
python3 -m unittest discover -v