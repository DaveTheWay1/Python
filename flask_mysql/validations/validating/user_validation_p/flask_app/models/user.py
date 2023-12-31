from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb = "user_validation"

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @staticmethod 
    def validate_create(user):
        is_valid = True
        if len(user["first_name"]) < 1:
            flash('Please enter your first name.')
            is_valid = False
        if len(user["last_name"]) < 1:
            flash('Please enter your last name.')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash('Please enter a valid email address.')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO 
                users(first_name, last_name, email, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM users
                '''
        results = connectToMySQL(mydb).query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users