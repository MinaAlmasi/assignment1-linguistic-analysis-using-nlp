#!/bin/bash

# create virtual environment
python3 -m venv env

# activate virtual environment 
source ./env/bin/activate

echo -e "[INFO:] Installing necessary requirements..."

# install reqs
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_md

# deactivate env 
deactivate

# celebratory user msg !
echo -e "[INFO:] Setup complete!"