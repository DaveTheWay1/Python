from flask_app.config.mysqlconnection import connectToMySQL
mydb  = "the_wall"
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]

    @staticmethod
    def validate_create(user):
        is_valid = True
        if len(user["first_name"]) < 1:
            flash('Please enter your first name')
            is_valid = False
        if len(user["last_name"]) < 1:
            flash('Please enter your last name')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash('Invalid email. Please enter a valid email')
            is_valid = False
        if len(user["password"]) <= 8:
            flash('Invalid password. Pleae enter a password with 8 charaters or more')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO 
                users(first_name, last_name, email, password, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data):
        query = '''
                SELECT * FROM users
                WHERE email = %(email)s:
                '''
        results = connectToMySQL(mydb).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_id(cls,data):
        query = '''
                SELECT * FROM users
                WHERE id = %(id)s
                '''
        results = connectToMySQL(mydb).query_db(query,data)
        return cls(results[0])