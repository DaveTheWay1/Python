from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

my_db = 'dojos_ninjas'
class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO dojos(name, created_at, updated_at)
                values(%(name)s, now(), now());
                '''
        return  connectToMySQL(my_db).query_db(query,data)
    
    @classmethod
    def get_one(cls, dojo_id):
        query = '''
                SELECT * FROM dojos
                WHERE id = %(id)s
                '''
        data = {
            "id": dojo_id
        }
        results = connectToMySQL(my_db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM dojos
                '''
        return connectToMySQL(my_db).query_db(query)
    
    @classmethod
    def update(cls, data):
        query = '''
                UPDATE dojos
                SET name = %(name)s
                WHERE id =  %(id)s
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_dojo_with_ninja(cls, dojo_id):
        query = '''
                SELECT * FROM dojos
                LEFT JOIN ninjas
                ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s
                '''
        data =  {
            "id": dojo_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        dojo = cls(results[0])
        for ninja_in_data in results:
            ninja_data = {
                "id":ninja_in_data["ninjas.id"],
                "first_name":ninja_in_data["first_name"],
                "last_name":ninja_in_data["last_name"],
                "age":ninja_in_data["age"],
                "created_at":ninja_in_data["ninjas.created_at"],
                "updated_at":ninja_in_data["ninjas.updated_at"]
            }
        dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo