from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Enable CORS for all routes
CORS(app)

# Graffiti Class/Model


class Graffiti(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firebase_id = db.Column(db.String(), db.ForeignKey(
        'user.firebase_id'), unique=False, nullable=False)
    drawing_str = db.Column(db.String(), unique=False, nullable=False)
    geo_lat = db.Column(db.Float, unique=False, nullable=False)
    geo_long = db.Column(db.Float, unique=False, nullable=False)
    votes = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.String(), unique=False, nullable=False)

    def __init__(self, firebase_id, drawing_str, geo_lat, geo_long, votes, created_at):
        self.firebase_id = firebase_id
        self.drawing_str = drawing_str
        self.geo_lat = geo_lat
        self.geo_long = geo_long
        self.votes = votes
        self.created_at = created_at

# Graffiti Schema


class GraffitiSchema(ma.Schema):
    class Meta:
        fields = ('id', 'firebase_id', 'drawing_str',
                  'geo_lat', 'geo_long', 'votes', 'created_at')


# Init schema
graffiti_schema = GraffitiSchema()
graffitis_schema = GraffitiSchema(many=True)

# Get endpoints.json
@app.route('/api', methods=['GET'])  # by default the method is get
def home():
    """Serves up a json file from the static folder"""
    return app.send_static_file('endpoints.json')

# Create Graffiti
@app.route('/api/graffiti', methods=['POST'])
def add_graffiti():
    """ Allows API user to post a new graffiti drawing to DB"""
    firebase_id = request.json['firebase_id']
    drawing_str = request.json['drawing_str']
    geo_lat = request.json['geo_lat']
    geo_long = request.json['geo_long']
    votes = request.json['votes']
    created_at = request.json['created_at']

    new_graffiti = Graffiti(firebase_id, drawing_str, geo_lat,
                            geo_long, votes, created_at)

    db.session.add(new_graffiti)
    db.session.commit()
    return graffiti_schema.jsonify(new_graffiti)

# Get All Graffiti
@app.route('/api/graffiti', methods=['GET'])
def get_graffitis():
    """ Gets all the graffiti drawings in the DB, returns empty array if none found"""
    all_graffiti = Graffiti.query.all()
    result = graffitis_schema.dump(all_graffiti)
    return jsonify(result)

# Get Single Graffiti
@app.route('/api/graffiti/<id>', methods=['GET'])
def get_graffiti(id):
    """ Gets a single graffiti id by its id"""
    single_graffiti = Graffiti.query.get(id)
    return graffiti_schema.jsonify(single_graffiti)

# Update Graffiti votes
@app.route('/api/graffiti/<id>', methods=['PUT'])
def update_graffiti_votes(id):
    """ Update specified graffiti vote count"""
    graffiti = Graffiti.query.get(id)
    votes = request.json['votes']
    graffiti.votes = votes
    db.session.commit()
    return graffiti_schema.jsonify(graffiti)

# Delete Graffiti
@app.route('/api/graffiti/<id>', methods=['DELETE'])
def delete_graffiti(id):
    """ Delete a single graffiti id by its id """
    graffiti = Graffiti.query.get(id)
    db.session.delete(graffiti)
    db.session.commit()
    return {'Message': 'The graffiti with id:{} has been deleted from records'.format(id)}

#############################################################

# User Class/Model


class User(db.Model):
    firebase_id = db.Column(db.String(), primary_key=True,
                            unique=True, nullable=False)
    username = db.Column(db.String(), unique=False, nullable=False)
    display_pic_url = db.Column(db.String(), unique=False, nullable=False)

    def __init__(self, firebase_id, username, display_pic_url):
        self.firebase_id = firebase_id
        self.username = username
        self.display_pic_url = display_pic_url


class UserSchema(ma.Schema):
    class Meta:
        fields = ('firebase_id', 'username',
                  'display_pic_url')


# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Create User
@app.route('/api/users', methods=['POST'])
def add_user():
    """ Allows API user to post a new user to DB"""
    firebase_id = request.json['firebase_id']
    username = request.json['username']
    display_pic_url = request.json['display_pic_url']
    new_user = User(firebase_id, username, display_pic_url)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

# Get All Users
@app.route('/api/users', methods=['GET'])
def get_users():
    """ Gets all the users in the DB, returns empty array if none found"""
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# Get Single User
@app.route('/api/users/<firebase_id>', methods=['GET'])
def get_user(firebase_id):
    """ Gets a single user id by their firebase_id"""
    single_user = User.query.filter_by(firebase_id=firebase_id)
    result = users_schema.dump(single_user)
    return jsonify(result[0])

# Update username
@app.route('/api/users/change_name/<firebase_id>', methods=['PUT'])
def update_username(firebase_id):
    """ Update specified user username"""
    user = User.query.filter_by(firebase_id=firebase_id)
    username = request.json['username']
    user[0].username = username
    result = users_schema.dump(user)
    db.session.commit()
    return jsonify(result)

# Update display_pic_url
@app.route('/api/users/change_pic/<firebase_id>', methods=['PUT'])
def update_display_pic(firebase_id):
    """ Update specified user display_pic"""
    user = User.query.filter_by(firebase_id=firebase_id)
    display_pic_url = request.json['display_pic_url']
    user[0].display_pic_url = display_pic_url
    result = users_schema.dump(user)
    db.session.commit()
    return jsonify(result)


# Delete User and All user graffiti (Cascade effect)
@app.route('/api/users/del/<firebase_id>', methods=['DELETE'])
def delete_user_graffiti(firebase_id):
    """ Delete a single user by their firebase_id and cascade delete all their drawings """
    Graffiti.query.filter_by(
        firebase_id=firebase_id).delete()
    User.query.filter_by(firebase_id=firebase_id).delete()

    db.session.commit()
    return {'Message': 'The user profile and graffiti associated with firebase_id = {} has been deleted from the database'.format(firebase_id)}


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
