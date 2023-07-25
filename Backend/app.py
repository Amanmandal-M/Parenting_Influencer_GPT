import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from middlewares.authentication_middleware import authentication_middleware
from controllers.responses_controller import prompt_controller, prompt_data_controller

# Importing all routes
from routes.user_route import user_router

app = Flask(__name__)
app.debug = True

# Enable CORS for all routes
CORS(app)

# Default route
@app.route('/')
def default_route():
    return '<h1 style="color: blue; text-align: center">Welcome to Parenting Influencer AI Backend!</h1>'

# Register the routes blueprints
app.register_blueprint(user_router, url_prefix='/user')

# Prompt routes
@app.route('/prompt', methods=['POST'])
@authentication_middleware
def protected_route():
    return prompt_controller()

@app.route('/prompt-data', methods=['GET'])
@authentication_middleware
def protected_data_route():
    return prompt_data_controller()

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Custom 405 error handler
@app.errorhandler(405)
def page_not_found(error):
    return render_template('405.html'), 405


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
