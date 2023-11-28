from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'pizza_restaurant'
class AddOns:
    def __init__(self, data):
        self.topping_id = data["topping_id"]
        self.pizza_id = data["pizza_id"]
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO add_ons(topping_id, pizza_id)
                values(%(topping_id)s, %(pizza_id)s)
                '''
        return connectToMySQL(my_db).query_db(query,data)