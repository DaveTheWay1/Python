from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import tweet

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.handle = data['handle']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # [] can represent a currently empty place to store all of the tweets that a single User instance has created, as a User creates MANY Tweets
        self.tweets = [] 

    @classmethod
    def save():
        query = '''
                INSERT INTO 
                users(first_name, handle, email, password, created_at, updated_at)
                values(%(first_name)s, %(handle)s, %(email)s, %(password)s, NOW(), NOW());
                '''
        return connectToMySQL()