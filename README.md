# Restul Flask API

## Pre-reqs:

- Python 3.6+
- pip

## When starting this project run the following commands in the terminal:

1. `pip install env`
2. `pipenv shell`
3. `pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy`

## Setting up db- run the following in the terminal:

1. `python`
2. `from app import db`
3. `db.create_all()`

If making any significant changes it is likely you will have to delete the db.sqlite file generated and re-run the above commands.
