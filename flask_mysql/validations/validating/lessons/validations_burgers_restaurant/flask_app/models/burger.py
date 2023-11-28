from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
my_db = 'restaurant_burgers'

# * 1 this burger will belong to a restaurant. though that is true, it does not
# * 2 mean that we will need to implement anyhting regarding the rest. in the variable methods below.

class Burger:
    def __init__(self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # * Static methods don't have self or cls passed into the parameters.
    # * We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_burger(burger):
        is_valid = True # we assume this is true
        if len(burger['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if int(burger['restaurant_id']) < 0:
            flash("Please select a Restaurant.")
            is_valid = False
        
        # the below is commented out bc they are not part of our database
        # but good to look at for refence/better understanding. more exmaples

        # if len(burger['bun']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # if int(burger['calories']) < 200:
        #     flash("Calories must be 200 or greater.")
        #     is_valid = False
        # if len(burger['meat']) < 3:
        #     flash("Meat must be at least 3 characters.")
        #     is_valid = False
        return is_valid

# * 3 it does though mean that we will need to implement something regarding that restaurant it belongs to
# * to tie the two together when we create(save) a burger into our database.
# * like shown in the classmethod below: 
    @classmethod
    def save(cls, data ):
        query = '''
                INSERT INTO 
                burgers (name, restaurant_id, created_at, updated_at ) 
                VALUES (%(name)s, %(restaurant_id)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM burgers
                '''
        results = connectToMySQL(my_db).query_db(query)
        burgers = []
        for burger  in results:
            burgers.append(burger)
        return burgers