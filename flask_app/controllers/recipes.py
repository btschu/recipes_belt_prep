from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_recipe.html', user = User.get_by_id(data))


@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "make_time": int(request.form["make_time"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    return redirect('/all_recipes')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html", edit = Recipe.get_one(data), user = User.get_by_id(user_data))

@app.route('/update/recipe',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "make_time": int(request.form["make_time"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/all_recipes')

@app.route('/recipe/<int:id>')
def one_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("one_recipe.html", recipe = Recipe.get_one(data), user = User.get_by_id(user_data))

@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/all_recipes')