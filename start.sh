#!/bin/sh
sleep 5
flask db upgrade
python3 -u remarkably/run.py