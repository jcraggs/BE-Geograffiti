# Geograffiti API

## Project Summary

Back end RESTful API built using python, flask and SQLite. It is hosted here: https://geograffiti.pythonanywhere.com/api

The repository of the front-end interacting with the hosted database, built by this application, can be found here: https://github.com/NaomiM24/geograffiti
The hosted front-end is here: https://geograffiti.netlify.com/

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
4. `pip freeze > requirements.txt`

This sets up the local pip environment and installs the required pip modules. Note that for the app to work you must be in the pipenv shell when you run `python app.py`.

## Setting up db.sqlite file

Run the following in the terminal:

1. `python`
2. `from app import db`
3. `db.create_all()`

If making any significant changes to routing and tables it is likely you will have to delete the db.sqlite file and re-run the above commands to generate a new one.

With the project and db.sqlite intialised you can start the local server by running `python app.py` in the terminal.

## Hosting a flask-app on 'PythonAnywhere'

Pre-reqs:

- PythonAnywhere Account (https://www.pythonanywhere.com/pricing/) -> click create beginner account

Prior to hosting, if you want to wipe your database, make sure to delete the old db.sqlite file and re-run the commands in the 'Setting up db.sqlite file' section.

1. Log into PythonAnywhere and select "\$Bash" from the 'New consoles' box
2. Choose the bash console and once open you will be able to git clone the repository to Python anywhere with: `git clone https://github.com/[git username]/[git project].git`
3. After cloning the repository into PythonAnywhere select "Web" from the menu tab

4. Click Add a new web app, then:

   - Ignore web-app domain name
   - Select Manual configuration from the web framework
   - Select your python version, this project was 3.6
   - Click next again to get PythonAnywhere to generate a template WSGI file for you. This will open your webapp configuration page.

5. Whilst on the configuration page link your source code to the project by editing the source code label in the 'Code' header on the page. The link should be something like '/home/[your_username]/[github_project_name]'

6. Edit the WSGI configuration file. You can access this by clicking on the link next to the "WSGI configuration file:" in your webapp view.

   Once you open the file you will need to comment/delete everything out and instead have the following:

   ```raw
   import sys

   path = '/home/geograffiti/BE-Geograffiti'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application  # noqa
   ```

   Note: the "/home/[username]" in the code above specifies your home directory -- the rest should be the directory you uploaded your Flask code to underneath the home directory. So if you just ran "git clone git@github.com/[username]/[git_project_name].git" then you should specify "/home/[username]/[git_project_name]".

   The from "app import app as application" essential renames the app = flask(**name**) within the app.py file to 'application'. This is required for the WSGI file to work.

7. You need to make sure that your app.py file does not have the following code:

   ```raw
   if __name__ == '__main__':
   app.run(debug=True)
   ```

   Whilst this is needed when running locally, it breaks the WSGI file when it comes to hosting on PythonAnywhere. You can edit your app.py file in PythonAnywhere by navigating to the directory of your project which will look something like: "https://www.pythonanywhere.com/user/[your_username]/files/home/[your_username]/[your_git_project_name]" and clicking on the edit icon next to the file name.

8. Set up your virtual environment by navigating back to the bash console as you did in step 1. Enter the following:

   - `mkvirtualenv myvirtualenv --python=/usr/bin/python3.6`

   Whilst still in the same console session run the following:

   - `pip install install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy gunicorn flask_cors`

   Further info on setting up a virtual env can be found here: https://help.pythonanywhere.com/pages/Virtualenvs/

9. Under the settings header on the web-app configuration page make sure to enable 'Force HTTPS'.

10. Finally click reload at the top of the web-app configuration page.

NOTE: PythonAnywhere web applications will timeout if you dont log in to the website at least once every 3 months.

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

- [AJINK13](https://github.com/AJINK13)
- [HAKeyes14](https://github.com/HAKeyes14)
- [jcraggs](https://github.com/jcraggs)
- [NaomiM24](https://github.com/NaomiM24)
