#!/bin/bash
kill $(ps ax | grep 'python home.py'| awk '{print $1}')
celery multi stopwait worker
