from flask_app.config.mysqlconnection import connectToMySQL
my_db = 'book_author_favorites'

class Favorite:
    def __init__(self, data):
        self.book_id = data["book_id"]
        self.author_id = data["author_id"]

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO 
                favorites(book_id, author_id)
                values(%(book_id)s, %(author_id)s);
                '''
        return connectToMySQL(my_db).query_db(query, data)