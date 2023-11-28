from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
mydb = ''

class Tweet:
    def __init__(self,data):
        self.id = data["id"]
        self.content = data["content"]
        self.location = data["location"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # None can represent a currently empty space 
        # for a single User dictionary to be placed here, 
        # as a Tweet is made by ONE User. We want a User 
        # instance and all their attributes to be placed here, 
        # so something like data['...'] will not work 
        # as we have to make the User instance ourselves.
        self.creator = None

    @staticmethod
    def validate_tweet(tweet):
        is_valid = True
        if len(tweet["content"]) < 1:
            flash('Please add content')
            is_valid = False
        if len(tweet["location"]) < 1:
            flash('Please add a location')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO 
                tweets(content, location, user_id, created_at, updated_at)
                values(%(content)s, %(location)s, %(user_id)s, NOW(),NOW());
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def get_all_tweets_with_creator(cls):
        # Get all tweets, and their one associated User that created it
        query = "SELECT * FROM tweets JOIN users ON tweets.user_id = users.id;"
        results = connectToMySQL('').query_db(query)
        all_tweets = []
        for tweet in results:
            # Create a Tweet class instance from the information from each db row
            one_tweet = cls(tweet)
            # Prepare to make a User class instance, looking at the class in models/user.py
            one_tweets_author_info = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": tweet['users.id'], 
                "name": tweet['name'],
                "handle": tweet['handle'],
                "email": tweet['email'],
                "password": tweet['password'],
                "created_at": tweet['users.created_at'],
                "updated_at": tweet['users.updated_at']
            }
            # Create the User class instance that's in the user.py model file
            author = user.User(one_tweets_author_info)
            # Associate the Tweet class instance with the User class instance by filling in the empty creator attribute in the Tweet class
            one_tweet.creator = author
            # Append the Tweet containing the associated User to your list of tweets
            all_tweets.append(one_tweet)
        return all_tweets
