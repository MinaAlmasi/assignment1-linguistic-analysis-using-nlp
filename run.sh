#!/bin/bash

# activate virtual environment (works only if setup.sh has been run !)
source ./env/bin/activate

# run code
echo -e "[INFO:] Running linguistic analysis ..." # user msg 
python3 src/extract_features.py

# deactivate virtual environment
deactivate

# celebratory user msg ! 
echo -e "[INFO:] Linguistic analysis complete!"