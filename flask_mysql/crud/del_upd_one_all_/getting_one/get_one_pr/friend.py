from mysqlconnection import connectToMySQL

class Friend:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        query ='''
                INSERT INTO 
                friends(first_name, last_name, occupation, created_at, updated_at) 
                values(%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());
                '''
        return connectToMySQL('first_flask').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM friends;
                '''
        results = connectToMySQL('first_flask').query_db(query)

        friends = []
        for friend in results:
            print(friend)
            friends.append(friend)
            print(friends)
        return friends
    
    @classmethod
    def get_one(cls, friend_id):
        query = '''
                SELECT * FROM friends where id = %(id)s;
                '''
        data = {
            "id": friend_id
        }
        results = connectToMySQL('first_flask').query_db(query, data)
        return cls(results[0])