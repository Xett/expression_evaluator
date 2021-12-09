#!/bin/bash

echo "Installing"
python3 -m pip install /vagrant

echo "Testing"
python3 /vagrant/tests/test.py