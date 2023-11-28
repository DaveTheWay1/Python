from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = "cookie_orders"

class Order:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.type = data["type"]
        self.num_of_boxes = data["num_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order["name"]) < 1:
            flash('Please add a name.')
            is_valid = False
        if len(order["type"]) < 3:
            flash('Please add a cookie type.')
            is_valid = False
        if int(order["num_of_boxes"]) < 0:
            flash('Please add amount of boxes')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO
                orders(name, type, num_of_boxes, created_at, updated_at)
                values(%(name)s, %(type)s, %(num_of_boxes)s, NOW(), NOW()); 
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM orders
                '''
        results = connectToMySQL(mydb).query_db(query)
        orders = []
        for order in results:
            orders.append(order)
        return orders
    
    @classmethod
    def get_one(cls,order_id):
        query = '''
                SELECT * FROM orders
                WHERE id = %(id)s
                '''
        data = {
            "id":order_id
        }
        results = connectToMySQL(mydb).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = '''
                UPDATE orders
                SET name = %(name)s, type = %(type)s, num_of_boxes = %(num_of_boxes)s
                WHERE id = %(id)s
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def delete(cls, order_id):
        query = '''
                DELETE FROM orders
                WHERE id = %(id)s
                '''
        data = {
            "id":order_id
        }
        return connectToMySQL(mydb).query_db(query, data)