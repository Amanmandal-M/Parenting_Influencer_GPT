import os
import bcrypt
import json
import jwt
from flask import jsonify,request
from models.all_model import userCollection, user_schema, validate_data
from bson import ObjectId, json_util


NORMAL_KEY = os.getenv('NORMAL_KEY')

# Controller: User Registration
# Method: POST
# Description: Registers a new user
def user_registration():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')
    location = data.get('location')
    country = data.get('country')

    requiredFields = {
        "name": name,
        "email": email,
        "gender": gender,
        "password": password,
        "location": location,
        "country":country
    }
    missingFields = []

    for field, value in requiredFields.items():
        if not value or value == "":
            missingFields.append(field)

    if len(missingFields) > 0:
        return jsonify({
            "success": False,
            "error": "Bad Request",
            "message": f"The following fields are missing: {', '.join(missingFields)}."
        }), 400

    try:
        # Validate user data against user schema
        valid = validate_data(data, user_schema)
        if not valid:
            return jsonify({"message": "Data validation failed"}), 400

        isPresent = userCollection.find_one({"email": email})
        if isPresent:
            return jsonify({"message": "User already exists"}), 401

        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(5))

        data = {
            "name": name,
            "email": email,
            "password": hash,
            "gender": gender,
            "location": location,
            "country":country
        }
        result = userCollection.insert_one(data)
        inserted_id = str(result.inserted_id)  # Convert ObjectId to string

        return jsonify({
            "success": True,
            "message": "User Registered Successfully",
            "data": {
                "_id": inserted_id,
                "name": name,
                "email": email,
                "gender": gender,
                "password": password,
                "location": location,
                "country":country
            }
        }), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Controller: User Login
# Method: POST
# Description: Performs user login
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    requiredFields = {
        "email": email,
        "password": password
    }
    missingFields = []

    for field, value in requiredFields.items():
        if not value or value == "":
            missingFields.append(field)

    if len(missingFields) > 0:
        return jsonify({
            "success": False,
            "error": "Bad Request",
            "message": f"The following fields are missing: {', '.join(missingFields)}."
        }), 400

    try:
        is_present = userCollection.find_one({"email": email})
        if not is_present:
            return jsonify({"message": "User not found"}), 401
        
        hashed_password = is_present.get('password')

        if bcrypt.checkpw(password.encode(), hashed_password):
            normal_token = jwt.encode({"masai": "masai"}, NORMAL_KEY, algorithm="HS256")

            # Convert is_present to JSON serializable format
            is_present_serializable = json_util.dumps(is_present)

            response = jsonify({
                "success": True,
                "message": "Login successful",
                "Token": normal_token,
                "Data": is_present_serializable
            })
            return response, 201
        else:
            return jsonify({"message": "Login failed"}), 404

    except Exception as e:
        return jsonify({"message": str(e)}), 500