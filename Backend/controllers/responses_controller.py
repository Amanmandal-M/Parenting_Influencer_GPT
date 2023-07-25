import os
import openai
import bcrypt
import jwt
from flask import jsonify, request, Flask
from models.all_model import promptCollection, prompt_schema, validate_data
from bson import ObjectId, json_util

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate completion using OpenAI API


def generate_completion(input_text, language):
    try:
        prompt = input_text
        max_tokens = 300
        n = 1

        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt},
                        {
                            "role": "system",
                            "content": "As an advanced Parenting Influencer AI, my mission is to provide expert guidance and valuable insights on parenting, child care, and family well-being. With an extensive knowledge base in the field of parenting, I am well-equipped to offer personalized responses tailored to your specific concerns and challenges related to raising children.\n\nFeel free to ask me anything related to parenting influencer topics, including child development, family dynamics, discipline, education, health, and emotional well-being. My purpose is to support you in creating a nurturing and enriching environment for your children, ensuring their happiness and overall well-being.\n\nHowever, it is important to note that my expertise is limited to parenting influencer topics. If you inquire about subjects unrelated to parenting or child care, such as information about celebrities, politicians, or any non-parenting matters, I regret to inform you that I do not have data or expertise in those areas. As a result, I won't be able to provide relevant responses to such questions.\n\nTo make the most of our interaction, let's focus on parenting influencer topics and work together to positively impact your parenting journey. Your questions and concerns related to parenting are of utmost importance to me, and I am dedicated to assisting you in every possible way.\n\nSo, go ahead and ask any parenting influencer question you may have, and together, we can create a meaningful and enriching parenting experience for you and your children. Let's join hands in nurturing the next generation and building a brighter future for families!"
                        }
                    ],
                    max_tokens=max_tokens,
                    n=n,
        )


        choices = response['choices']
        if choices and len(choices) > 0:
            completion = choices[0]['message']['content'].strip()
            return completion
        else:
            return False
    except Exception as error:
        print("Error:", error)
        return None



def prompt_controller():
    try:
        data = request.get_json()
        question = data.get('question')
        language = data.get('language')
        user_id = request.user_id

        # Generate code conversion completion
        response = generate_completion(question,language)

        # Validate user data against user schema
        # valid = validate_data(data, prompt_schema)
        # if not valid:
        #     return jsonify({"message": "Data validation failed"}), 400

        dataBody = {
            "user_id": user_id,
            'question': question,
            'language': language,
            'convertedCode': response
        }

        result = promptCollection.insert_one(dataBody)
        return jsonify(response=response), 200
    except Exception as error:
        print("Error:", error)
        return jsonify(error="An error occurred"), 500
    
    
def prompt_data_controller():
    user_id = request.user_id
    # Use a dictionary to define the query with user_id field
    query = {"user_id": user_id}
    
    # Use find() with the query to get the data
    data = promptCollection.find(query)
    
    # Convert the data to a list, and use json_util to serialize the ObjectId to JSON
    data_list = list(data)
    serialized_data = json_util.dumps(data_list)
    
    # Return the serialized data as JSON
    return jsonify(success=True, data=serialized_data), 200
