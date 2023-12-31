from mysqlconnetion import connectToMySQL
my_db = "users_py_cl"

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO
                users(first_name, last_name, email, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM users;
                '''
        results = connectToMySQL(my_db).query_db(query)

        users = []
        for user in results:
            users.append(user)
        return users
    
    @classmethod
    def update(cls, data):
        query = '''
                UPDATE users 
                set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_one(cls, user_id):
        query = '''SELECT * FROM users
                    WHERE id = %(id)s
                '''
        data = {
            "id":user_id
        }
        results = connectToMySQL(my_db).query_db(query,data)
        
        return cls(results[0])
    
    @classmethod
    def delete(cls, user_id):
        query = '''
                DELETE FROM users
                WHERE id = %(id)s
                '''
        data = {
            "id":user_id
        }
        return connectToMySQL(my_db).query_db(query, data)
