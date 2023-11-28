from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = '''INSERT INTO 
                    users (username, email, password, created_at, updated_at) 
                    VALUES (%(username)s, %(email)s, %(password)s, NOW(), NOW());
                '''
        return connectToMySQL("mydb").mysql.query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # * if it Didn't find a matching user:
        if len(result) < 1:
            return False
        return cls(result[0])