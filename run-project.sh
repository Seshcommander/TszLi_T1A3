#!/bin/bash -e
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py 
deactivate



