from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'dojos_ninjas'
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO
                ninjas(first_name, last_name, age, dojo_id, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = '''
                UPDATE ninjas
                SET first_name = %(first_name)s,last_name = %(last_name)s,age = %(age)s, dojo_id = %(dojo_id)s
                WHERE id = %(id)s
                '''
        return connectToMySQL(my_db).query_db(query,data)
    
    @classmethod
    def delete(cls, user_id):
        query = '''
                DELETE FROM ninjas
                WHERE ninjas.id = %(id)s
                '''
        data = {
            "id":user_id
        }
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM ninjas
                '''
        results = connectToMySQL(my_db).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def get_one(cls, user_id):
        query = '''
                SELECT * FROM ninjas
                WHERE id = %(id)s
                '''
        data  =  {
            "id":user_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        return cls(results[0])