#!/bin/bash
#
# * Launch "crontab -e" and add the script:
#
# Important:
# - Ensure that the file has the execute bit set.
#
# Resubmit logs
# 1 * * * * ~/code/saja-expo-api/serverconfig/cron/resubmit.sh > /dev/null 2>&1

source ~/virtualenvs/saja-expo-api/bin/activate
cd ~/code/saja-expo-api
python manage.py resubmit
deactivate
