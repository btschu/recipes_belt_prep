from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.make_time = data['make_time']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipe_schema').query_db(query)
        recipes = []
        for recipe in recipes:
            recipes.append( cls(user))
        return recipes

    # @classmethod
    # def get_user_messages(cls,data):
    #     query = "SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id =  %(id)s"
    #     results = connectToMySQL('recipe_schema').query_db(query,data)
    #     messages = []
    #     for message in results:
    #         messages.append( cls(message) )
    #     return messages

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name,description,instructions, date_made, make_time, user_id) VALUES (%(name)s,%(desctiption)s,%(instructions)s,%(date_made)s,%(make_time)s,%(user_id)s);"
        return connectToMySQL('recipe_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE recipe.id = %(id)s;"
        return connectToMySQL('recipe_schema').query_db(query,data)