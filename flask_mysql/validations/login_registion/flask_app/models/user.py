from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = 'bcrypt_schema'

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_create(user):
        is_valid = True
        if len(user["username"]) < 1:
            flash('Please enter a username')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash('Please enter a valid email')
            is_valid = False
        if len(user["password"]) < 8:
            flash('Please enter a password of at least 8 characters')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO 
                users (username, email, password, created_at, updated_at)
                values (%(username)s, %(email)s, %(password)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = '''
                SELECT * FROM users
                where email = %(email)s
                '''
        results = connectToMySQL(mydb).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,user_id):
        query = '''
                SELECT * FROM users
                where id = %(id)s
                '''
        results = connectToMySQL(mydb).query_db(query, user_id )
        return cls(results[0])
