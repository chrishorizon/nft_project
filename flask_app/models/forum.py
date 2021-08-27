from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
import re
bcrypt = Bcrypt(app)

LETTERS_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        # self.first_name = data['first_name']
        # self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (username, email, password) VALUES (%(username)s, %(email)s, %(password)s)"
        return connectToMySQL('nifty').query_db(query, data)

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM users"
        results = connectToMySQL('nifty').query_db(query, data)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod 
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        
        results = connectToMySQL('nifty').query_db(query, data)

        if not results or len(results) == 0: 
            return False
        else:
            return cls(results[0])