# Geograffiti API

## Project Summary

Back end RESTful API built using python, flask and SQLite. It is hosted here: https://be-geograffiti.herokuapp.com/api

This project was built using the help of the following video tutorial: https://www.youtube.com/watch?v=PTZiDnuC86g

## How to run this project:

Download the project repo:

1. Click on the repo's "Clone or Download" button link and copy the URL (https://github.com/jcraggs/BE-Geograffiti.git)
2. Navigate to where you'd like the application to be copied in your command line and write:

   ```
   git clone https://github.com/jcraggs/BE-Geograffiti.git
   ```

Pre-reqs

- Python 3.6+
- pip

When starting this project locally run the following commands in the terminal:

1. `pip install env`
2. `pipenv shell`
3. `pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy gunicorn flask_cors`

This sets up the local pip environment and installs the required pip modules.

## Setting up db.sqlite file

Run the following in the terminal:

1. `python`
2. `from app import db`
3. `db.create_all()`

If making any significant changes to routing and tables it is likely you will have to delete the db.sqlite file and re-run the above commands to generate a new one.

With the project and db.sqlite intialised you can start the local server by running `python app.py` in the terminal.

## Hosting on Heroku

Pre-reqs:

- Heroku Account (https://signup.heroku.com/)
- Installed Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)

Prior to hosting, if you want to wipe your database, make sure to delete the old db.sqlite file and re-run the commands in the 'Settin up db.sqlite file' section.

1. `pip freeze > requirements.txt`
2. Create a 'Procfile' in the root directory and populate it with the following plain text: "web: gunicorn app:app"
3. Log into Heroku and select New -> Create new app
4. `heroku login -i`
5. `heroku git:remote -a {name of the heroku app}`
6. `git push heroku master`
7. `heroku open`

Further information on how to host can be found here: https://stackabuse.com/deploying-a-flask-application-to-heroku/

## Current endpoints

| Endpoint                            | Request | Response                                                                                                                              |
| ----------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| /api                                | GET     | Serves up a JSON representation of all the available endpoints of the API.                                                            |
| /api/graffiti                       | GET     | Serves an array of all graffiti data.                                                                                                 |
| /api/graffiti                       | POST    | Posts a single graffiti object with contents dependent on the post request body sent.                                                 |
| /api/graffiti/:graffiti_id          | GET     | Serves an object with the specified graffiti information.                                                                             |
| /api/graffiti/:graffiti_id          | PUT     | Serves an updated graffiti object with the 'votes' key changed by the value specified in the request body.                            |
| /api/graffiti/:graffiti_id          | DELETE  | Serves an object with the specified graffiti information.                                                                             |
| /api/users                          | GET     | Serves an array of all the users in the database.                                                                                     |
| /api/users                          | POST    | Adds a user to the database, the firebase_id must be unique.                                                                          |
| /api/users/:firebase_id             | GET     | Serves an object with the specified users information.                                                                                |
| /api/users/change_name/:firebase_id | PUT     | Serves an updated user object with the 'username' key changed by the value specified in the request body.                             |
| /api/users/change_pic/:firebase_id  | PUT     | Serves an updated user object with the 'display_pic_url' key changed by the value specified in the request body.                      |
| /api/users/del/:firebase_id         | DELETE  | Deletes the user by specified user_id, cascade deletes all their drawings and returns an object with a message confirming the action. |

## Project Team

- [AJINK14](https://github.com/AJINK13)
- [HAKeyes14](https://github.com/HAKeyes14)
- [jcraggs](https://github.com/jcraggs)
- [NaomiM24](https://github.com/NaomiM24)
