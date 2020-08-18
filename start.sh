#!/bin/sh
flask db upgrade
python3 -u remarkably/run.py