from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'restaurant_burgers'
from flask_app.models import burger

class Restaurant:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # * We create a list so that later we can add in all the burgers that are associated with a restaurant.
        self.burgers = []

    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO restaurants(name, created_at, updated_at)
                values(%(name)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM restaurants
                '''
        results = connectToMySQL(my_db).query_db(query)

        restaurants =  []
        for restaurant in results:
            restaurants.append(restaurant)
        return restaurants
    
    @classmethod
    def get_restaurant_with_burgers(cls, restaurant_id ):
        query = '''
                SELECT * FROM restaurants 
                LEFT JOIN burgers 
                ON burgers.restaurant_id = restaurants.id 
                WHERE restaurants.id = %(id)s;
                '''
        data = {
            "id":restaurant_id
        }
        results = connectToMySQL(my_db).query_db(query, data )
        # results will be a list of topping objects with the burger attached to each row. 
        restaurant = cls(results[0])
        for burg_data in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            burger_data = {
                # * as we already have an id in this restaurant file, we need to specify that we are referencing 
                # * the burgers id and not the restaurant id like we do so below. 
                # * THE SAME APPLIES FOR ALL DATA VARIABLES WITH MATCHING NAMES 
                "id": burg_data["burgers.id"],
                "name": burg_data["burgers.name"],
                # * WHEN THERE IS DATA VARIABLES WITHOUT MATCHING NAMES WE INCLUDE THEM LIKE SO.
                # * in this case, we have them highlighted out bc we did not include these
                # * when createing our table.
                #  "bun": row_from_db["bun"],
                # "meat": row_from_db["meat"],
                # "calories": row_from_db["calories"],
                "created_at": burg_data["burgers.created_at"],
                "updated_at": burg_data["burgers.updated_at"]
            }
            restaurant.burgers.append(burger.Burger( burger_data))
        return restaurant