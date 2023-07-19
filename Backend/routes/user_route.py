from flask import Blueprint, request, jsonify
from controllers.user_controller import user_registration, user_login

# Create a Blueprint for the user routes
user_router = Blueprint('user', __name__)

# Route: User Registration
# Method: POST
# Description: Registers a new user
user_router.route('/register', methods=['POST'])(user_registration)

# Route: User Login
# Method: POST
# Description: Performs user login
user_router.route('/login', methods=['POST'])(user_login)
