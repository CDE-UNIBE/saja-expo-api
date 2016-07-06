#!/bin/bash
# activate virtualenv, run migrations and touch uwsgi to reload the application server.
APP_BASE=/srv/wnf-proxy-app
APP_HOME=${APP_BASE}/app
echo "updating proxy app"
cd $APP_HOME
git pull origin master
source /srv/wnf-proxy-app/env/bin/activate  && python /srv/wnf-proxy-app/app/manage.py migrate
sudo service uwsgi restart 
sudo service nginx restart
