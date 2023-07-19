from flask import Blueprint
from controllers.responses_controller import prompt_controller

# Create a Blueprint for the user routes
response_router = Blueprint('prompt', __name__)

# Route: User Registration
# Method: POST
# Description: Registers a new user
response_router.route('/', methods=['POST'])(prompt_controller)
