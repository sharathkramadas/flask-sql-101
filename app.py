from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{0}:{1}@{2}:3306/{3}'.format(DATABASE_USERNAME,DATABASE_PASSWORD,DATABASE_HOST,DATABASE_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, first_name, last_name, email):
    	self.first_name = first_name
    	self.last_name = last_name
    	self.email = email

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

@app.route('/users/create', methods=['POST'])
def create():
	first_name = request.json.get('first_name')
	last_name = request.json.get('last_name')
	email = request.json.get('email')
	user = User(first_name=first_name, last_name=last_name, email=email)
	db.session.add(user)
	db.session.commit()	
	return jsonify({'message':'User created successfully!'})

@app.route('/users/read/<int:pk>', methods=['GET'])
def read(pk):	
	user = User.query.filter(User.id == pk).first()	
	data = {
		'first_name':user.first_name,
		'last_name':user.last_name,
		'email':user.email,
	}	
	return jsonify(data)

@app.route('/users/update/<int:pk>', methods=['PUT'])
def update(pk):
	first_name = request.json.get('first_name')
	last_name = request.json.get('last_name')
	email = request.json.get('email')	
	user = User.query.filter(User.id == pk).first()	
	user.first_name = first_name
	user.last_name = last_name
	user.email = email
	db.session.commit()
	return jsonify(request.json)

@app.route('/users/delete/<int:pk>')
def delete():
	user = User.query.filter(User.id == pk).first()
	db.session.delete(user)	
	db.session.commit()	
	return jsonify({'message':'User deleted successfully!'})

@app.route('/users/list',methods=['GET'])
def list():
	users = User.query.all()	
	result = [{'id':u.id,'first_name':u.first_name,'last_name':u.last_name,'email':u.email} for u in users]	
	return jsonify(result)	

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)