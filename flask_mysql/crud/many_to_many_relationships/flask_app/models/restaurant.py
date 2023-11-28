from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import pizza
my_db = 'pizza_restaurant'

class Restaurant:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.pizzas = []

    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO
                restaurants(name, created_at, updated_at)
                values(%(name)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * from restaurants
                '''
        results = connectToMySQL(my_db).query_db(query)
        restaurants = []
        for restaurant in results:
            restaurants.append(restaurant)
        return restaurants
    
    @classmethod
    def get_restaurant_with_pizza(cls,restaurant_id):
        query = '''
                SELECT * FROM restaurants
                LEFT JOIN pizzas
                ON pizzas.restaurant_id = restaurants.id
                WHERE restaurants.id = %(id)s
                '''
        data = {
            "id": restaurant_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        restaurant = cls(results[0])
        for pizza_in_data in results:
            pizza_data = {
                "id":pizza_in_data["pizzas.id"],
                "name":pizza_in_data["pizzas.name"],
                "size":pizza_in_data["size"],
                "crust":pizza_in_data["crust"],
                "created_at":pizza_in_data["pizzas.created_at"],
                "updated_at":pizza_in_data["pizzas.updated_at"]
            }
            restaurant.pizzas.append(pizza.Pizza(pizza_data))
        return restaurant
