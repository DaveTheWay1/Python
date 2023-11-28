from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'restaurant_burgers'

# * 1 this burger will belong to a restaurant. though that is true, it does not
# * 2 mean that we will need to implement anyhting regarding the rest. in the variable methods below.

class Burger:
    def __init__(self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
