
# ? 1. What is the difference between this creator query, 

@classmethod
def get_post_with_creator(cls):
    query = '''
            SELECT * FROM posts
            LEFT JOIN users 
            ON posts.user_id = users.id
            '''
    results = connectToMySQL(mydb).query_db(query)
    all_posts = []
    for post in results:
        one_post = cls(post)
        none_to_creator = {
            "id":post["users.id"],
            "first_name":post["first_name"],
            "last_name":post["last_name"],
            "email":post["email"],
            "password":post["password"],
            "created_at":post["users.created_at"],
            "updated_at":post["users.updated_at"]
        }
        author = user.User(none_to_creator)
        one_post.creator = author
        all_posts.append(one_post)
    return all_posts


# ? 2. the many to many relationship query,  

    self.toppings = []

@classmethod
def get_pizza_with_topping(cls,pizza_id):
    query = '''
            SELECT * FROM pizzas
            LEFT JOIN add_ons
            ON add_ons.pizza_id = pizzas.id 
            LEFT JOIN toppings 
            ON add_ons.topping_id = toppings.id
            WHERE pizzas.id = %(id)s
            '''
    data = {
        "id":pizza_id
    }
    results = connectToMySQL('').query_db(query, data)
    pizza = cls(results[0])

    for topping_in_data in results:
        toppings_data = {
            "id": topping_in_data["toppings.id"],
            "name":topping_in_data["name"],
            "created_at":topping_in_data["toppings.created_at"],
            "updated_at":topping_in_data["toppings.created_at"]
        }
        pizza.toppings.append(topping.Topping(toppings_data))
    return pizza

# ? 3. and one to many relationship query?

# self.burgers = []

@classmethod
def get_restaurant_with_burger(cls,restaurant_id):
    query = '''
            SELECT * FROM restaurants
            LEFT JOIN burgers
            ON burgers.restaurant_id = restaurants.id
            WHERE restaurants.id = %(id)
            '''
    data ={
        "id":restaurant_id
    }
    results = connectToMySQL('').query_db(query,data)
    restaurant = cls(results[0])
    for burger_in_data in results:
        burger_data = {
            "id":burger_in_data["burgers.id"],
            "name":burger_in_data["name"],
            "created_at":burger_in_data["burgers.created_at"],
            "updated_at":burger_in_data["burgers.updated_at"]
        }
        restaurant.burgers.append(burger.Burger(burger_data))
    return restaurant

# Well, lets take a look...

# * the MANY TO MANY QUERY inclues an additonal table
# * to combine the two tables creating a many to many.
# we had that many pizzas can have many toppings
# and the many toppings can go on many pizzas. 
# to combine the two, we did a one to many for both
# (creating that many to many) but instead of connecting
# to each other we used a table (add_ons) to connect 
# the two togther
# * ADDTIONALLY, we do require a WHERE (pizza.id = %(id)s)
# * for this QUERY unlike the the post creator query that does not
#  overall, it comes down to what the developer wants to be displayed.
# if it wanted to refer to a specific post then it would 
# require the where and done more similar to the pizzas query

# * OUR RESULTS is done the same as our pizzas method. right after our
# * query

# * THOUGH, for our posts method, we list is created for hold our posts
# * upon completion of the method.
# there is a list here and not a list on the pizzas because, again,
# this query references to get many while the pizzas method querry
# references to get one specific

# * our choice of usering one_post = cls(post) inside the for loop
# * and our cls(results[0]) outside the for loop revolves around the same 
# * concept
# the post method querry refers to the findings of many posts, not just one specific
# so we have it set up to reference for every post
# our pizzas method query looks for one specific pizza findings hence
# why it is set up the way it is, to relate it all to one specific pizza

# * AFTER FOR LOOP FOR POST

# * we leave space for the data we wish to attach the same way.
# * author data is implemented the same way as topping data

# * we pass in our data author in user.User() as we save it in a variable
# * called author.
# * we grab the one post and grap its sub variable of creator -> one_post.creator
# * and set that to our author change the one_post.creator = None being set
# * to the author data we just collected per post relating to its belonging post
# * upon doing that we append that one post to our all_posts empty list created in the for loop
# * and finallly return the final product of that (all_posts) one the for loop is complete

# * VS

# * AFTER FOR LOOP FOR PIZZA
# * we grab the singular pizza instance, refer back to our toppings = []
# * empty list and save the topping data to our toppings table
# * finally, we return that final product of pizza

# * the difference is that posts is working with a singular, relating every post
# * to a SINGLE creator WHILE the pizzas is relating a list of toppings to one pizza

# ? Remaining: What is the difference between this posts method query/
# ? many to many methods query, and the one to many methods query?
# * the same differences exist from post to many to many(pizzas) from the 
# * one to many except, as a one to many, it does not include another table
# * in the query like the many to many query. other than that it is just like the many to many query was ran
# * if it did not have a where required it would be just like the post query(similar
# * if we were also referencing many and not just singular