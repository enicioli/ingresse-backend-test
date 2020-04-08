#!/bin/bash

if [ "$FLASK_ENV" = "development" ]
then
  pip3 install -r requirements-dev.txt
  python3 ./indexes.py all
  python3 ./import.py
fi