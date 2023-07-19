import os
from flask import Flask
from flask_cors import CORS

# All routes imported
from routes.responses_route import response_router
from routes.user_route import user_router


app = Flask(__name__)

app.debug = True

# Enable CORS for all routes
CORS(app)

# Default routes
@app.route('/')
def default_routes():
    return '<h1 style="color:blue;text-align:center">Welcome to Parenting Influencer AI Backend!</h1>'

# Register the routes blueprint
app.register_blueprint(user_router, url_prefix='/user')
app.register_blueprint(response_router, url_prefix='/prompt')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
