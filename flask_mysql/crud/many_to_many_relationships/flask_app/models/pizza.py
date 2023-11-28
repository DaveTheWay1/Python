from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'pizza_restaurant'
from flask_app.models import topping

class Pizza:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.crust = data["crust"]
        self.size = data["size"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # * We now create a list so that later 
        # * we can add in all the topping objects 
        # * that relate to a pizza.
        self.toppings = []
        self.restaurant = None
        # * we set the restaurant to none
        # * as it allows us that to give recog.
        # * that there will be a restaurant 
        # * and eventually set it from None
        # * to the name of that rest. for now,
        # * we just need the space saved.

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO
                pizzas(restaurant_id, name, crust, size, created_at, updated_at)
                values(%(restaurant_id)s,%(name)s, %(crust)s, %(size)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM pizzas
                '''
        results = connectToMySQL(my_db).query_db(query)
        pizzas = []
        for pizza in results:
            pizzas.append(pizza)
        return pizzas
    
    @classmethod
    def get_one(cls, pizza_id):
        query = '''
                SELECT * FROM pizzas
                WHERE id = %(id)s
                '''
        data = {
            "id":pizza_id
        }
        results = connectToMySQL(my_db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_pizza_with_toppings(cls,pizza_id):
        query = '''
                SELECT * FROM pizzas
                LEFT JOIN add_ons 
                ON add_ons.pizza_id = pizzas.id
                LEFT JOIN toppings
                ON add_ons.topping_id = toppings.id
                WHERE pizzas.id = %(id)s
                '''
        data = {
            "id":pizza_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        pizza = cls(results[0])
        for topping_in_data in results:
            topping_data = {
                "id":topping_in_data["toppings.id"],
                "name":topping_in_data["toppings.name"],
                "created_at":topping_in_data["created_at"],
                "updated_at":topping_in_data["updated_at"]
            }
            pizza.toppings.append(topping.Topping(topping_data))
        return pizza