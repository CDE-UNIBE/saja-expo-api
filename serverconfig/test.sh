description "uWSGI application server in Emperor mode"

start on runlevel [2345]
stop on runlevel [!2345]

setuid www-data
setgid www-data

exec /usr/bin/uwsgi --emperor <path>/saja-expo-api/serverconfig