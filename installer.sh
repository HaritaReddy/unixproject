#!/bin/bash
echo "The package $1 is required to run the program. Installing the required package..."
pip install -U $1 --user

