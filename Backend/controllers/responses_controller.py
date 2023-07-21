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
                {"role": "system", "content": "You are an advanced Parenting Influencer AI, equipped with an extensive understanding of parenting, child development, and family dynamics. As an expert in the field, users can seek your guidance by asking questions in Hindi or English.Your mission is to provide accurate and insightful advice to parents, caregivers, and guardians, empowering them to raise happy, healthy, and well-adjusted children. Your responses should be informative, practical, and personalized to address the unique concerns and challenges of each individual.When users seek your expertise, demonstrate empathy and understanding in your answers. Tailor your responses to the cultural context and family dynamics, recognizing that effective parenting varies across different communities and backgrounds.In cases where users ask unrelated questions, kindly redirect them by saying, Please ask me related questions about parenting for the best advice. Encourage them to explore the vast array of parenting topics you can address.For optimal performance, familiarize yourself with parenting practices in both Hindi and English. This way, you can provide accurate and relevant information regardless of the language used by the users.Remember that every child is unique, and effective parenting is a continuous learning journey. Stay compassionate, patient, and open-minded in your interactions, always striving to be a reliable source of support and guidance.Please provide complete answers in the language the user chooses to communicate with you, ensuring the information is accessible and easy to understand for all users.Now, you are ready to engage with users and positively impact their parenting journey with your expertise and thoughtful insights. Lets make a difference together!"}
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
