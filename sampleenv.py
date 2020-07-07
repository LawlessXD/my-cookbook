# This is a sample environment variable file
# If deploying locally, this file should be renamed as env.py
import os, secrets

# MONGO_URI environment variable
# Replace <username>,<password>,<clustername>,<dbname> with the relevants values for your Database
os.environ["MONGO_URI"] = "mongodb+srv://<username>:<password>@<clustername>-8wcdt.mongodb.net/<dbname>?retryWrites=true&w=majority"
# This generates a random secret key required for session cookie
os.environ["SECRET_KEY"] = secrets.token_urlsafe(16)
# Replace <dbname with relevant value for your Database
os.environ["MONGO_DBNAME"] = "<dbname>"
