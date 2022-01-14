from flask import render_template,redirect,session,request, flash
import re
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

@app.route('/save_recipe', methods=['POST'])
def save_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "user_id": request.form['user_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    Recipe.save(data)
    return redirect('/all_recipes')

@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    data = {
        "id": id
    }
    Recipe.destroy(data)
    return redirect('/all_recipes')