from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
my_db = ('dojos_ninjas')

class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age =  data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.dojos = []

    @classmethod
    def save(cls, data):
                query = '''
                        INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at)
                        values(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, now(), now());
                        '''
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
    def get_one(cls, ninja_id):
        query = '''
                SELECT * FROM ninjas
                WHERE id = %(id)s
                '''
        data = {
            "id":ninja_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_ninja_with_dojo(cls,ninja_id):
        query = '''
                SELECT * FROM ninjas
                LEFT JOIN dojos 
                ON dojos.id = ninjas.dojo_id
                WHERE
                ninjas.id = %(id)s
                '''
        data = {
            "id": ninja_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        ninja = cls(results[0])
        for dojo_in_data in results:
            dojo_data = {
                "id" : dojo_in_data["dojos.id"],
                "name" : dojo_in_data["name"],
                "created_at": dojo_in_data["dojos.created_at"],
                "updated_at": dojo_in_data["dojos.updated_at"]
            }
        ninja.dojos.appened(dojo.Dojo(dojo_data))
        return ninja
    
    @classmethod
    def update(cls, data):
        query = '''
                UPDATE ninjas
                SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
                WHERE id = %(id)s
                '''
        return connectToMySQL(my_db).query_db(query, data)


