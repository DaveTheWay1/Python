from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
my_bd = 'users_cl_py'
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email =  data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def validate_user(user):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSET INTO 
                users(first_name, last_name, email, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
                '''
        return connectToMySQL(my_bd).query_db(query, data)