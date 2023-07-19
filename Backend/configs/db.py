import os
from pymongo import MongoClient

Mongo_link = os.getenv('MONGO_URI')

# Establish connection to MongoDB
client = MongoClient(Mongo_link)
db = client['InfluencerDb']

# Export the database connection
dbConnection = db
