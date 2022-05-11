from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_bcrypt import Bcrypt

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


def __init__(self, username, password, email):
    self.username = username
    self.password = password
    self.email = email


class UserSchema(ma.Schema):

    class Meta:
        fields = ('id', 'username', 'password', 'email')


user_schema = UserSchema()
multi_user_schema = UserSchema(many=True)

# # Endpoint to add a user
@app.route('/user/add', methods=['POST'])
def add_user():
    if request.content_type != 'application/json':
        return jsonify('Error: This is embarrassing...maybe you should, I dunno...TRY IT AS JSON!')

    post_data = request.get_json()
    username = post_data.get('username')
    password = post_data.get('password')
    email = post_data.get('email')

    if username == None:
        return jsonify('Error: Provide A Username, ya DINGUS!')
    if password == None:
        return jsonify('Error: Provide A Password, ya DINGUS!')
    if email == None:
        return jsonify('Error: Provide An Email Address, ya DINGUS!')
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')


    new_user = User(username, pw_hash, email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))

# Verification Endpoint
@app.route('user/verify', methods=['POST'])
def verify():
    if request.content_type != 'application/json':
        return jsonify('Error: This is embarrassing...maybe you should, I dunno...TRY IT AS JSON!')

    post_data = request.get_json()
    username = post_data.get_json('username')
    password = post_data.get_json('password')

    user = db.session.query(User).filter(User.username == username).first()

    if user is None:
        return jsonify('Look what you did! You might be a user, but you couldn\'t be verified...')
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify('Look what you did! You might be a user, but you couldn\'t be verified...')
    
    return jsonify('That\'s right, you\'re verified!')

# # Endpoint to query all users
@app.route('/user-roster/get', methods=['GET'])
def get_all_users():
    all_users = db.session.query(User).all()
    return jsonify(multi_user_schema.dump(all_users))

# # Endpoint to query one user
@app.route('/user/get/<id>', methods=['GET'])
def get_user_id(id):
    one_user = db.session.query(User).filter(User.id == id).first()
    return jsonify(user_schema.dump(one_user))

# # Endpoint to delete a user
@app.route('/user/delete/<id>', methods=['DELETE'])
def user_to_delete(id):
    delete_user = db.session.query(User).filter(User.id == id).first()
    db.session.delete(delete_user)
    db.session.commit()
    return jsonify("You are not the user you once were...You're GONE!")

# # Endpoint to update/edit a user
@app.route('/user/update/<id>', methods=['PUT'])
def update_user_id(id):
    if request.content_type != 'application/json':
        return jsonify('Error: This is embarrassing...maybe you should, I dunno...TRY IT AS JSON!')

    put_data = request.get_json()
    username = put_data.get('user')
    pw_hash = put_data.get('pw_hash')
    email = put_data.get('email')

    user_to_update = db.session.query(User).filter(User.id == id).first()

    if username != None:
        user_to_update.username = username
    if pw_hash != None:
        user_to_update.pw_hash = pw_hash
    if email != None:
        user_to_update.email = email

    db.session.commit()
    return jsonify(user_schema.dump(user_to_update))



if __name__ == '__main__':
    app.run(debug=True)