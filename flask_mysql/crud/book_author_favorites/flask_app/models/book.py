from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
my_db = 'book_author_favorites'

class Book:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.pages = data["pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors = []
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT INTO 
                books(name, pages, created_at, updated_at)
                values(%(name)s, %(pages)s, NOW(), NOW());
                '''
        return connectToMySQL(my_db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT * FROM books
                '''
        results = connectToMySQL(my_db).query_db(query)
        books = []
        for book in results:
            books.append(book)
        return books
    
    @classmethod
    def get_book_with_favorites(cls,book_id):
        query = '''
                SELECT * FROM books
                LEFT JOIN favorites
                ON favorites.book_id = books.id
                LEFT JOIN authors
                ON favorites.author_id = authors.id 
                WHERE books.id = %(id)s
                '''
        data = {
            "id":book_id
        }
        results = connectToMySQL(my_db).query_db(query, data)
        book = cls(results[0])
        for author_in_results in results:
            author_data = {
                "id":author_in_results["authors.id"],
                "first_name":author_in_results["first_name"],
                "last_name":author_in_results["last_name"],
                "created_at":author_in_results["authors.created_at"],
                "updated_at":author_in_results["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book