import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "myCookBook"
MONGODB_URI = os.environ.get("MONGO_URI") 
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/recipe/<recipe_id>')
def view_recipe(recipe_id):
    return render_template("viewrecipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)