from mysqlconnection import connectToMySQL
my_db = 'first_flask'
class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# * we create a classmethod called get_all to get all the friends 
# * listed in our data base.
    @classmethod
    def get_all(cls):
        # * we create our variable called query which 
        # * will contain our query that will get all
        query = "SELECT * from friends;"

        # * we create another variable called results which
        # * will hold our results of the query
        results = connectToMySQL(my_db).query_db(query)
        # ! EXPLAING RESULTS
        # * STEP ONE:
        # * our results variable is able to get the results
        # * as we first call the function from mysqlconnection.py

        # * within mysqlconnection.py is the function; connectToMySQL. 
        # * as we call the function in line 22, we pass in our database.
        # * (above we set the variable my_db to equal the name of our database)

        # * STEP TWO:
        # * Within the connectToMySQL function is another function called
        # * query_db. we call it as it takes in a query and we pass in our 
        # * query there.

        # * IN SUMARRY:
        # * with the calling of connectToMySQL and query_db function, we are
        # * running a function which connects our code to our MySQL database 
        # * (connectToMySQL) which then allows for our query to be ran with the 
        # * following function being called (query_db)


        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends
    
        # * as this is a get all. we create a variable which contains an empty list
        # * we then create a for loop to go through our results
        # * as we loop through, we want to add every friend to our list known as the variable friends
        # * once complete, we return that list; friends

    @classmethod
    def save(cls,data):
        query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) values(%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"
        return connectToMySQL(my_db).query_db(query, data)
    
    # * BREAK DOWN:
    # * we create a classmethod to save data inserted by the user.
    # * we call it save and pass in the class and data.
    # * we create a variable called query which contains the query needed to save data.
    # * we do this succsfully be using prepared statements within the query. Prepared statements help prevent users to be able to type in dangerous sql.
    # * since we just want it to save within our data base, we dont need to save it into a variable but only
    # * return (calls) the functions that does the saving

    # * the function; connectToMySQL which connects our code to the database or MySQL.
    # * AND the following function which, after being connected to our database/MySQL,
    # * allows for our written query stored in our variable "query" to run