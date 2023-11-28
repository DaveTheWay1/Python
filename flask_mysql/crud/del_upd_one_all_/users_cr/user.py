from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO users(first_name, last_name, email, created_at, updated_at)
                values (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());
                '''
        return connectToMySQL('users_py_cl').query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * from users;
                '''
        results = connectToMySQL('users_py_cl').query_db(query)

        users = []
        for user in results:
            users.append(user)
        return users
    
    @classmethod
    def get_one(cls, user_id):
        query = '''
                SELECT  * FROM users where id = %(id)s;
                '''
        data = {
            "id":user_id
        }
        results = connectToMySQL('users_py_cl').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = '''
                UPDATE users set first_name = %(fname)s, last_name = %(lname)s, email = %(email)s
                WHERE id = %(id)s;
                '''
        return connectToMySQL('users_py_cl').query_db(query,data)
    
    @classmethod
    def delete(cls, delete_id):
        query = "DELETE FROM users where id = %(id)s;"
        data = {
            "id":delete_id
        }
        return connectToMySQL('users_py_cl').query_db(query,data)
