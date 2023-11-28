from mysqlconnection import connectToMySQL

class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = "insert into friends(first_name, last_name, occupation, created_at, updated_at) values(%(frsname)s, %(lsname)s, %(occ)s, NOW(), NOW());"
        return connectToMySQL('first_flask').query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "select * from friends"
        results = connectToMySQL('first_flask').query_db(query)

        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends
    
    @classmethod
    def get_one(cls,friend_id):
        query  = "SELECT * from friends where id = %(identification)s;"
        data = {
            "identification":friend_id
        }
        results = connectToMySQL('first_flask').query_db(query, data)
        print(results)
        return cls(results[0])
        
        # * we doing the return:
        # must return with class or it wont display on html like desired
        # must include an index or else you'll get an error for it
        # index must be of 0; anyhting else is out of list range