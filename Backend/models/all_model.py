from configs.db import dbConnection
from bson import ObjectId

# Get the collections
userCollection = dbConnection["user"]
promptCollection = dbConnection["prompt"]

# Define the user schema
user_schema = {
    "name": str,
    "email": str,
    "password": str,
    "gender": str,
    "location": str,
    "country": str
}

# Define the prompt schema
prompt_schema = {
    "userId": ObjectId,
    "question": str,
    "language": str
}

# Function to validate the data against the schema
def validate_data(data, schema):
    for key, value_type in schema.items():
        if key not in data or not isinstance(data[key], value_type):
            return False
    return True

# Export the collections and schemas
__all__ = ["userCollection", "promptCollection",
           "user_schema", "prompt_schema", "validate_data"]
