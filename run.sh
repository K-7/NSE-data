#!/bin/bash
source env/bin/activate
celery multi start worker -A scrap -B --autoscale=4,1 --loglevel=INFO
python home.py