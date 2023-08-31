# Getting Started with JUICEME

This project was create with JUICEME Team


# How to run this project ?

# There are two folders (backend => django and frontend => reactjs)

# 0. Python version 3.11.4

# 1. Run the django project

- Go to backend project 
- Create a virtualenv
	## virtualenv venv
- Activate the venv
	## source venv/bin/activate
- Install dependences
	## pip install -r requirements.txt
- Create a postgres database (name: juiceme_db, user: baimi, password: baimi)
	## sudo -u postgres psql
	## CREATE DATABASE juiceme_db;
	## CREATE USER baimi WITH PASSWORD 'baimi';
	## ALTER ROLE baimi SET client_encoding TO 'utf8';
	## ALTER ROLE baimi SET default_transaction_isolation TO 'read committed';
	## ALTER ROLE baimi SET timezone TO 'UTC';
	## GRANT ALL PRIVILEGES ON DATABASE juiceme_db TO baimi;
	## \q
- Execute makemigrations
	## python manage.py makemigrations
- Execute migrate
	## python manage.py migrate
- Create a superuser
	## python manage.py createsuperuser
- Execute runserver
	## python manage.py runserver
- On browser go to http://127.0.0.1:8000 to simple portal
- On browser go to http://127.0.0.1:8000/en/admin to admin portal

# 2. Run the reactjs project

- Go to frontend
- Inatll dependences 
	## npm i
- Run the server
	## npm run serve
- On browser go to http://127.0.0.1:3000

# ENJOY :-)
