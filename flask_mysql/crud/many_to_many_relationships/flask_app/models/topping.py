from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'pizza_restaurant'
from flask_app.models import pizza

class Topping:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        # we need have a list in case we want to show which pizza are related to the topping.
        self.on_pizzas = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO 
                toppings(name, created_at, updated_at)
                values(%(name)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM toppings
                '''
        results = connectToMySQL(my_db).query_db(query)
        toppings = []
        for topping in results:
            toppings.append(topping)
        return toppings
    
    @classmethod
    def get_topping_with_pizza(cls,topping_id):
        query = '''
                SELECT * FROM toppings 
                LEFT JOIN add_ons 
                ON add_ons.topping_id = toppings.id
                LEFT JOIN pizzas 
                ON add_on.pizza_id = pizzas.id
                WHERE id = %(id)s
                '''
        data = {
            "id":topping_id
        }
        results = connectToMySQL(my_db).query_db(query,data)
        topping = cls(results[0])
        for pizza_in_data in results:
            pizza_data = {
                "id":pizza_in_data["pizzas.id"],
                "name":pizza_in_data["name"],
                "crust":pizza_in_data["crust"],
                "size":pizza_in_data["size"],
                "created_at":pizza_in_data["pizzas.created_at"],
                "updated_at":pizza_in_data["pizzas.updated_at"]
            }
            topping.on_pizzas.append(pizza.Pizza(pizza_data))
        return topping