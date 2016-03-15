#saja-expo-api

Internal API between expo and myswissalps.

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb saja_expo
```
Initialize the git repository

```
git init
git remote add origin git@github.com:CDE-UNIBE/saja-expo-api.git
```

Migrate the database and create a superuser:
```bash
python saja_expo/manage.py migrate
python saja_expo/manage.py createsuperuser
```

Run the development server: 
```bash
python saja_expo/manage.py runserver
```
