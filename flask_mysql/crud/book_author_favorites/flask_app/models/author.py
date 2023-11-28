from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
my_db = 'book_author_favorites'
class Author:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books = []

    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO 
                authors(first_name, last_name, created_at, updated_at)
                values(%(first_name)s, %(last_name)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM authors
                '''
        results = connectToMySQL(my_db).query_db(query)
        authors = []
        for author in results:
            authors.append(author)
        return authors
    
    @classmethod
    def get_author_with_favorites(cls, author_id):
        query = '''
                SELECT * FROM authors
                LEFT JOIN favorites
                ON favorites.author_id = authors.id
                LEFT JOIN books
                ON favorites.book_id = books.id
                WHERE authors.id = %(id)s
                '''
        data = {
            "id":author_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        author = cls(results[0])
        for book_in_results in results:
            book_data = {
                "id":book_in_results["books.id"],
                "name":book_in_results["name"],
                "pages":book_in_results["pages"],
                "created_at":book_in_results["books.created_at"],
                "updated_at":book_in_results["books.updated_at"]
            }
            author.books.append(book.Book(book_data))
        return author