from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    """Factory to create and configure the Flask app."""
    app = Flask(__name__)

    # Set secret key and configurations
    app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_default_secret_key')  # Replace with a strong key
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'audio/')
    app.config['ALLOWED_EXTENSIONS'] = {'wav', 'mp3', 'm4a'}

    # Register blueprints if using modular structure (Optional)
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
