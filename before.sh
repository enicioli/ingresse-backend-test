#!/bin/bash

python3 ./indexes.py

if [ "$FLASK_ENV" = "development" ] ; then python3 ./import.py ; fi

exec "$@"