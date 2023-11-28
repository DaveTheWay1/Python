from flask_app.models import recipe
from flask_app import app
from flask import render_template, redirect, request, session

@app.route('/create/recipe')
def create_recipe():
    return render_template('create_recipe.html')

@app.route('/save/recipe', methods = ["POST"])
def save_recipe():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/create/recipe')
    data = {
        "name":request.form["name"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "user_id":session["user_id"]
    }
    recipe.Recipe.save(data)
    return redirect('/home')

@app.route('/view/recipe/<recipe_id>')
def view_recipe(recipe_id):
    selected_recipe = recipe.Recipe.getById(recipe_id)
    print(selected_recipe)
    return render_template('recipe.html', recipe = selected_recipe)

@app.route('/search', methods = ["POST"])
def search_recipe():
    data = request.form["name"]
    searched_recipe = recipe.Recipe.getByName(data)
    return redirect(f'/view/recipe/{searched_recipe.id}')

@app.route('/edit/<recipe_id>')
def edit_page(recipe_id):
    selected_recipe = recipe.Recipe.getById(recipe_id)
    return render_template('edit.html', recipe = selected_recipe)

@app.route('/save/edit', methods = ["POST"])
def save_edit():
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    recipe.Recipe.edit(request.form)
    return redirect(f'/view/recipe/{request.form["id"]}')

@app.route('/delete/<recipe_id>')
def delete_recipe(recipe_id):
    recipe.Recipe.delete(recipe_id)
    return redirect('/home')