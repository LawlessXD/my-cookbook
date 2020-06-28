import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") 
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
@app.route('/recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("viewrecipe.html",recipe=recipe)

@app.route('/addrecipe')
def add_recipe():
    # Check if user is not logged in already
    if 'user' in session:
        return render_template("addrecipe.html") 
    else:
        flash('You must be logged in before you can add a recipe')
        return redirect(url_for('login'))

@app.route('/saverecipe',methods=['POST'])
def save_recipe():
    if 'user' not in session:
        flash('You must be logged in before you can add or save a recipe')
        return redirect(url_for('login'))
    if request.method == 'POST':
        new_recipe = {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_image': request.form.get('recipe_image'),
            'recipe_type': request.form.get('recipe_type'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_author': session['user'],
            'recipe_prep_time': request.form.get('recipe_prep_time'),
            'recipe_cook_time': request.form.get('recipe_cook_time'),
            'recipe_skill_level': request.form.get('recipe_skill_level'),
            'recipe_serving': request.form.get('recipe_serving'),
            'ingredients': request.form.getlist('ingredient'),
            'method': request.form.getlist('step')
        }
        result = mongo.db.recipes.insert_one(new_recipe)
        if result.inserted_id:
            flash('Recipe has been successfully added.')
            return redirect(url_for('get_recipes'))
        else:
            flash('There was an issue saving your recipe, please try again.')
            return redirect(url_for('add_recipe'))  

@app.route('/editrecipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    if session['user'] != recipe['recipe_author']:  
        flash("Only the author can edit or delete a recipe")
        return redirect(url_for('view_recipe',recipe_id=recipe_id))
    else:
        recipe_types = {'Breakfast','Lunch','Dinner','Dessert','Snack'}
        skill_level = {'Easy','Medium','Hard'}
    return render_template("editrecipe.html", recipe=recipe, recipe_types=recipe_types, skill_level=skill_level)  

@app.route('/updaterecipe/<recipe_id>',methods=['POST'])
def update_recipe(recipe_id):
        if 'user' not in session:
            flash('You must be logged in before you can update a recipe')
            return redirect(url_for('login'))
        if request.method == 'POST':
            mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
                {   
                    'recipe_name': request.form.get('recipe_name'),
                    'recipe_image': request.form.get('recipe_image'),
                    'recipe_type': request.form.get('recipe_type'),
                    'recipe_description': request.form.get('recipe_description'),
                    'recipe_author': session['user'],
                    'recipe_prep_time': request.form.get('recipe_prep_time'),
                    'recipe_cook_time': request.form.get('recipe_cook_time'),
                    'recipe_skill_level': request.form.get('recipe_skill_level'),
                    'recipe_serving': request.form.get('recipe_serving'),
                    'ingredients': request.form.getlist('ingredient'),
                    'method': request.form.getlist('step')
                })
        return redirect(url_for('get_recipes'))

@app.route('/login', methods=['GET','POST'])
def login():
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/
    if 'user' in session:
        isUser = mongo.db.users.find_one({'username': session['user']})
        if isUser:
            flash(f"You are already logged in as {session['user']}, please logout to sign in as a different user.")
            return redirect(url_for('get_recipes'))
    if request.method == 'POST':
        # retrieve the data from the login form
        username = request.form.get('username').lower()
        password = request.form.get('password').lower()
        # Check if user is in the DB
        isUser = mongo.db.users.find_one({'username': username})
        if isUser:
            # Check if the password entered matches the passowrd in DB
            if check_password_hash(isUser['password'],password):
                # Add username to session variable user
                session['user'] = username
                session['first'] = isUser['firstname']
                flash("You have been successfully logged in!")
                return redirect(url_for('get_recipes'))
            else:
                flash("Invalid Password, please check and try again!")
                return redirect(url_for('login'))
        else:
            flash("Invalid Username, please check and try again!")    
            return redirect(url_for('login'))
        # show the login form    
    return render_template("login.html")

@app.route('/register', methods=['GET','POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already signed in')
        return redirect(url_for('get_recipes'))
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/
    if request.method == 'POST':
        # retrieve the data from the registration form
        username = request.form.get('username').lower()
        password = request.form.get('password').lower()    
        confirm_password = request.form.get('confirm_password').lower()
        firstname = request.form.get('firstname').lower()
        lastname = request.form.get('lastname').lower()
        email = request.form.get('email').lower()
        # Check if the passwords entered match
        if password== confirm_password:
            # Check the username does not exist already
            isUser = mongo.db.users.find_one({'username': username})
            if isUser:
                flash(f"{username} already exists, please choose a different username.")
                return redirect(url_for('register'))
            # If user does not exist then add the user to the DB
            else:
                hashed_password = generate_password_hash(password,method='pbkdf2:sha256')
                mongo.db.users.insert_one(
                    {
                        'username': username,
                        'password': hashed_password,
                        'firstname': firstname,
                        'lastname': lastname,
                        'email': email
                    }
                )
                # Check if the user has been saved in the DB
                isUser = mongo.db.users.find_one({'username': username})
                if isUser:
                    # Add user to the session variable User
                    session['user'] = username
                    return redirect(url_for('get_recipes'))
                else:
                    flash("There was an issue saving your details, please try again.")
                    return redirect(url_for('register'))
        else:
            flash("Passwords entered do not match, please verify and try again.")
            return redirect(url_for('register'))

    return render_template("register.html") 

# Log out
@app.route('/logout')
def logout():
	# Clear the session
	session.clear()
	flash('You have been successfully logged out, see you again soon!')
	return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)