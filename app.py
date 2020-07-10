import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
# Import env.py for environment variables when running app locally
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# Environment Variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") 
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# route decorator for recipes which returns all recipes in the DB
@app.route('/')
@app.route('/recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

# route decorator for a single recipe, view_recipe takes recipe_id as an input
# view_recipe uses recipe_id to find the associated recipe in the DB
@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("viewrecipe.html",recipe=recipe)

# route decorator for adding a recipe
@app.route('/addrecipe')
def add_recipe():
    # If the user is logged in render the addrecipe HTML template, otherwise redirect to login 
    if 'user' in session:
        return render_template("addrecipe.html") 
    else:
        flash('You must be logged in before you can add a recipe')
        return redirect(url_for('login'))

# route decorator for saving a recipe to the DB from the add recipe form
@app.route('/saverecipe',methods=['POST'])
def save_recipe():
    # Redirect the user if not signed in
    if 'user' not in session:
        flash('You must be logged in before you can add or save a recipe')
        return redirect(url_for('login'))
    # When the form is submitted, create a new document new_recipe with the fields in JSON format
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
        # Insert new document into recipes collection
        result = mongo.db.recipes.insert_one(new_recipe)

        # If the document was inserted successfully, redirect to recipes page and display a success message
        # If the document insert fails, redirect to add_recipe form  
        if result.inserted_id:
            flash('Recipe has been successfully added.')
            return redirect(url_for('get_recipes'))
        else:
            flash('There was an issue saving your recipe, please try again.')
            return redirect(url_for('add_recipe'))  

# route decorator for editing a recipe
# edit_recipe function takes recipe ID as an argument
@app.route('/editrecipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    # If the user in session doesn't match the author, redirect to the recipe and display a message
    if session['user'] != recipe['recipe_author']:  
        flash("Only the author can edit or delete a recipe")
        return redirect(url_for('view_recipe',recipe_id=recipe_id))
    else:
        # Variables for dropdown fields
        recipe_types = {'Breakfast','Lunch','Dinner','Dessert','Snack'}
        skill_level = {'Easy','Medium','Hard'}
    # render edit recipe template with parameters
    return render_template("editrecipe.html", recipe=recipe, recipe_types=recipe_types, skill_level=skill_level)

# route decorator for deleting a recipe
# delete_recipe function takes recipe ID as an argument
@app.route('/deleterecipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    # If the user in session doesn't match the author, redirect to the recipe and display a message
    if session['user'] != recipe['recipe_author']:  
        flash("Only the author can edit or delete a recipe")
        return redirect(url_for('view_recipe',recipe_id=recipe_id))
    else:
    # If the current user is the author, remove the recipe and return to the recipes page
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        flash('Recipe has been successfully deleted.')
        return redirect(url_for('get_recipes'))

# Route decorator for editing a recipe
# update_recipe function takes recipe ID as an argument
@app.route('/updaterecipe/<recipe_id>',methods=['POST'])
def update_recipe(recipe_id):
        # Redirect the user if not signed in
        if 'user' not in session:
            flash('You must be logged in before you can update a recipe')
            return redirect(url_for('login'))
        if request.method == 'POST':
            # Updtae the recipe with the fields from the edit recipe form
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

# Credit - https://github.com/MiroslavSvec/DCD_lead for login functionality
# Credit - https://flask.palletsprojects.com/en/1.1.x/quickstart/
# route decorator for login
@app.route('/login', methods=['GET','POST'])
def login():
    # If the user is already in the session variable, advise the user that they are already logged in
    # redirect the user to recipes page
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
                # Add username to session variable user and redirect to recipes page
                session['user'] = username
                session['first'] = isUser['firstname']
                flash("You have been successfully logged in!")
                return redirect(url_for('get_recipes'))
            else:
                flash("Invalid login details, please check and try again!")
                return redirect(url_for('login'))
        else:
            flash("Invalid login details, please check and try again!")    
            return redirect(url_for('login'))
    # show the login form if method is get    
    return render_template("login.html")

# route decorator for register 
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
        password1 = request.form.get('password1').lower()    
        password2 = request.form.get('password2').lower()
        firstname = request.form.get('firstname').lower()
        lastname = request.form.get('lastname').lower()
        email = request.form.get('email').lower()
        # Check if the passwords entered match
        if password1 == password2:
            # Check the username does not exist already
            isUser = mongo.db.users.find_one({'username': username})
            if isUser:
                flash(f"{username} already exists, please choose a different username.")
                return redirect(url_for('register'))
            # If user does not exist then add the user to the DB
            else:
                # Generate hash of the password entered
                hashed_password = generate_password_hash(password1,method='pbkdf2:sha256')
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
                    session['first'] = firstname
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

# Setting debug to false for production environment i.e. Heroku
# If running this application locally, set debug to True for troubleshooting
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=False)