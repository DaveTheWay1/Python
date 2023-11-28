from flask_app.config.mysqlconnection import connectToMySQL
mydb = 'the_wall'
from flask import flash
from flask_app.models import user
class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None

    @staticmethod
    def validate_post(post):
        is_valid = True
        if len(post["content"]) < 1:
            flash('Post content must not be left blank')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO
                posts(content, user_id, created_at, updated_at)
                values(%(content)s, %(user_id)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM posts
                '''
        results = connectToMySQL(mydb).query_db(query)
        all_posts = []
        for post in results:
            all_posts.append(post)
        return all_posts
    
    @classmethod
    def post_and_creator(cls):
        # * first we set the query to get all posts info including related users
        query = '''
                SELECT * FROM posts
                LEFT JOIN users
                ON posts.user_id = users.id
                '''
        # * next we save the results into our results as we will eventually loop through it
        results = connectToMySQL(mydb).query_db(query)
        # * then we create where we will store our findings
        all_posts = []
        # * but we also need to help specify our findings and get to them
        # * so we create a for loop, create the variable post to reference 
        # *  each of our findings in results
        for post in results:
            # * we create the instance of a post
            one_post = cls(post)

            # * we define dictionary for the author so the post may
            # * reach all of the info
            posts_with_author = {
                "id": post["users.id"],
                "first_name": post["first_name"],
                "last_name":post["last_name"],
                "email": post["email"],
                "password":post["password"],
                "created_at":post["users.created_at"],
                "updated_at":post["users.updated_at"]
            }
            # * we legitmize the author by passing the dictionary 
            # * into the user class
            author = user.User(posts_with_author)
            # * we save the author to our instance of a post
            # * and connect it to our self.creator so 
            # * our post understands that all that info
            # * belongs to the creator.
            one_post.creator = author
            # * finally, now that all has been filled,
            # * (post infomation and now including the creator)
            # * we can append our findings to our all_posts 
            all_posts.append(one_post)
        # * and we return our findings
        return all_posts
    
    @classmethod
    def post_creator(cls):
        query = '''
                SELECT * FROM posts
                LEFT JOIN users
                ON posts.user_id = users.id
                '''
        results = connectToMySQL(mydb).query_db(query)
        all_posts = []

        for post in results:
            one_post = cls(post)
            author_data = {
                "id": post["users.id"],
                "first_name": post["first_name"],
                "last_name":post["last_name"],
                "email":post["email"],
                "password":post["password"],
                "created_at":post["users.created_at"],
                "updated_at":post["users.updated_at"]
            }
            author = user.User(author_data)
            one_post.creator = author
            all_posts.append(one_post)
        return all_posts
    