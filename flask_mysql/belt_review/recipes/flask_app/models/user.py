from flask_app.config.mysqlconnection import connectToMySQL
mydb = 'recipes_again'
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
        self.updated_at = data["updated_at"]
    
    @staticmethod
    def validate_create(user):
        is_valid = True
        if len(user["first_name"]) < 1:
            flash('Please add your first name')
            is_valid = False
        if len(user["last_name"]) < 1:
            flash('Please add your last name')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash('Invalid email')
            is_valid = False
        if len(user["password"]) < 8:
            flash('Please add a password of at least 9 characters')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO
                users(first_name, last_name, email, password, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def getByEmail(cls,data):
        query = '''
                SELECT * FROM users
                WHERE email = %(email)s
                '''
        results = connectToMySQL(mydb).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def getById(cls,data):
        query = '''
                SELECT * FROM users
                WHERE id = %(id)s 
                '''
        results = connectToMySQL(mydb).query_db(query,data)
        return cls(results[0])