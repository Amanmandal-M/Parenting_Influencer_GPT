import os
import openai
import bcrypt
import jwt
from flask import jsonify,request
from models.all_model import promptCollection, prompt_schema, validate_data
from bson import ObjectId, json_util

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[],
#   temperature=1,
#   max_tokens=200,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

def prompt_controller():
  user_id = request.user_id
  return jsonify(user_id)