#!/bin/bash
#
# * Launch "crontab -u www-data -e" and add the script:
#
# Important:
# - Ensure that the file has the execute bit set.
#
# Resubmit logs
# 0 9 * * * ~/code/saja-expo-api/serverconfig/cron/remove_stale.sh > /dev/null 2>&1

. /srv/wnf-proxy-app/env/bin/activate
cd /srv/wnf-proxy-app/app
python manage.py remove_stale
deactivate
