from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'recipes_again'
from flask_app.models import user

class Recipe:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 1:
            flash('Please enter a recipe name')
            is_valid = False
        if len(recipe["description"]) < 1:
            flash('Please enter a description')
            is_valid = False
        if len(recipe["instructions"]) < 1:
            flash('Please enter instructions')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls,data):
        query = '''
                INSERT INTO recipes(name, description, instructions, user_id, created_at, updated_at)
                values(%(name)s, %(description)s, %(instructions)s, %(user_id)s, NOW(), NOW());
                '''
        return connectToMySQL(mydb).query_db(query,data)
    
    @classmethod
    def get_recipe_with_creator(cls):
        query = '''
                SELECT * FROM recipes
                LEFT JOIN users 
                ON recipes.user_id = users.id
                '''
        results = connectToMySQL(mydb).query_db(query)
        recipes = []
        for recipe in results:
            one_recipe = cls(recipe)
            creator_data = {
                "id":recipe["users.id"],
                "first_name":recipe["first_name"],
                "last_name":recipe["last_name"],
                "email":recipe["email"],
                "password":recipe["password"],
                "created_at":recipe["users.created_at"],
                "updated_at":recipe["users.updated_at"]
            }
            author = user.User(creator_data)
            one_recipe.creator = author
            recipes.append(one_recipe)
        return recipes
    
    @classmethod
    def getByName(cls,name):
        query = '''
                SELECT * FROM recipes
                WHERE name = %(name)s
                '''
        data = {
            "name":name
        }
        results = connectToMySQL(mydb).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def getById(cls,recipe_id):
        query = '''
                SELECT * FROM recipes
                LEFT JOIN users
                ON recipes.user_id = users.id 
                WHERE recipes.id = %(id)s
                '''
        data = {
            "id": recipe_id
        }
        results = connectToMySQL(mydb).query_db(query, data)
        recipe = cls(results[0])
        for post in results:
            creator_data = {
                "id":post["users.id"],
                "first_name":post["first_name"],
                "last_name":post["last_name"],
                "email":post["email"],
                "password":post["password"],
                "created_at":post["users.created_at"],
                "updated_at":post["users.updated_at"]
            }
            author = user.User(creator_data)
            recipe.creator = author
        return recipe
    
    @classmethod
    def edit(cls, data):
        query = '''
                UPDATE recipes
                SET name = %(name)s, description = %(description)s, instructions = %(instructions)s
                WHERE recipes.id = %(id)s
                '''
        return connectToMySQL(mydb).query_db(query, data)
    
    @classmethod
    def delete(cls,recipe_id):
        query = '''
                DELETE FROM recipes
                WHERE recipes.id = %(id)s
                '''
        data = {
            "id":recipe_id
        }
        return connectToMySQL(mydb).query_db(query, data)
