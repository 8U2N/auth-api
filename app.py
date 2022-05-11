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


# class Name(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     value1 = db.Column(db.String, unique=True, nullable=False)
#     value2 = db.Column(db.Integer, unique=True, nullable=True)


# def __init__(self, value1, value2, author):
#     self.value1 = value1
#     self.value2 = value2


# class NameSchema(ma.Schema):

# class Meta:
#     fields = ('id', 'Value1', 'Value2')


# name_schema = NameSchema()
# multi_name_schema = NameSchema(many=True)

# # Endpoint to add a value
# @app.route('/value/add', methods=['POST'])
# def add_value():
#     if request.content_type != 'application/json':
#         return jsonify('Error: data MUST be sent as JSON!')

#     post_data = request.get_json()
#     value1 = post_data.get('value1')
#     value2 = post_data.get('value2')

#     if value1 == None:
#     return jsonify('Error: Thou Shalt Provide A Value1!')
#     if title == None:
#     return jsonify('Error: Thou Shalt Provide A Value2!')

#     new_record = Name(value1, value2)
#     db.session.add(new_record)
#     db.session.commit()

# return jsonify(name_schema.dump(new_record))


# # Endpoint to query all values
# @app.route('/value/get', methods=['GET'])
# def get_all_values():
#     all_records = db.session.query(Name).all()
#     return jsonify(multi_name_schema.dump(all_records))

# # Endpoint to query one value
# @app.route('/value/get/<id>', methods=['GET'])
# def get_value_id(id):
#     one_value = db.session.query(Name).filter(Name.id == id).first()
#     return jsonify(name_schema.dump(one_value))

# # Endpoint to delete a value
# @app.route('/value/delete/<id>', methods=['DELETE'])
# def value_to_delete(id):
#     delete_value = db.session.query(Name).filter(Name.id == id).first()
#     db.session.delete(delete_value)
#     db.session.commit()
#     return jsonify("The value you chose is POOF! Gone, done, DELETED!")

# # Endpoint to update/edit a value
# @app.route('/value/update/<id>', methods=['PUT'])
# def update_value_id(id):
#     if request.content_type != 'application/json':
#     return jsonify('Error: data must be sent as JSON!')

#     put_data = request.get_json()
#     value1 = put_data.get('value1')
#     value2 = put_data.get('value2')

#     value_to_update = db.session.query(Name).filter(Name.id == id).first()

#     if value1 != None:
#     value_to_update.value1 = value1
#     if value2 != None:
#     value_to_update.value2 = value2

# db.session.commit()

# return jsonify(value_schema.dump(value_to_update))

if __name__ == '__main__':
    app.run(debug=True)