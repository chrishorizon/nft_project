from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
import re
bcrypt = Bcrypt(app)

LETTERS_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$')

class Forum:
    def __init__(self,data):
        self.title = data['title']
        self.topic = data['topic']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO forums (title, topic, description) VALUES (%(title)s, %(topic)s, %(description)s)"
        return connectToMySQL('nifty').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM forums"
        results = connectToMySQL('nifty').query_db(query)
        forums = []
        for row in results:
            forums.append( cls(row))
        return forums


    @staticmethod
    def valid_post(post):
        is_valid = True 

        if not len(post['title']) > 0:
            flash('Title is required', 'title')
            is_valid = False

        if not len(post['topic']):
            flash('Topic is required', 'topic')
            is_valid = False
        elif len(post['topic']) < 3:
            flash('Topic must be at least 3 characters', 'topic')
            is_valid = False

        if not len(post['description']):
            flash("Description is required", 'description')
            is_valid = False
        elif len(post['description']) < 8:
            flash("Description must be at least 8 characters", 'description')
            is_valid = False

        return is_valid

