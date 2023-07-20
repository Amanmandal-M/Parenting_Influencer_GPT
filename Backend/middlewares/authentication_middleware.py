import jwt
from flask import jsonify, request
from functools import wraps
import os

# Middleware decorator function
def authentication_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Get the token from the request headers
            token = request.headers.get('Authorization')

            if not token:
                return jsonify({"error": "Unauthorized", "message": "Token not provided"}), 401

            # Remove the 'Bearer ' prefix from the token if present
            if token.startswith('Bearer '):
                token = token.split('Bearer ')[1]

            # Verify the token using the secret key
            secret_key = os.getenv('NORMAL_KEY')
            decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

            # Extract the user ID from the decoded token
            user_id = decoded_token.get('user_id')

            # Attach the user ID to the request object for further use in route handlers
            request.user_id = user_id

        except jwt.ExpiredSignatureError:
            # Token has expired
            return jsonify({"error": "Unauthorized", "message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            # Invalid token
            return jsonify({"error": "Unauthorized", "message": "Invalid token"}), 401

        # Call the route handler
        return f(*args, **kwargs)

    return decorated_function
