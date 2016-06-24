#saja-expo-api

Internal API for communication between the expo and myswissalps.

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- A file-based storage is used by default.

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```

Add the folder 'apps' to the path

- if virtualenvwrapper is available: ```add2virtualenv apps```
- without virtualenv: ```echo "`pwd`/apps" > <yourvirtualenv>/<yoursitepackages>/_apps_path.pth``` (or just add the path to your python-path)

Install dependencies:
```bash
pip install -r requirements/local.txt
```

Initialize the git repository

```
git init
git remote add origin git@github.com:CDE-UNIBE/saja-expo-api.git
```

Migrate the database and create a superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```

Set the environment variables:

- envs/DATABASE_URL = ```sqlite:////<some-local-path>```.
  (For a proper database, refer to [dj-database-url](https://github.com/kennethreitz/dj-database-url))
- envs/API_URL = ```dev.myswissalps.ch```

# Run the project

Run the development server: 
```bash
python manage.py runserver
```

Run the production server:

- Use (maybe symlink) the files ```serverconfig/uwsgi.ini``` and ```serverconfig/nginx-vhost.conf```
- Install the crontab: resubmit.sh
