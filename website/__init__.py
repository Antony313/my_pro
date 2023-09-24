from flask import Flask, render_template, request, redirect, url_for
from database import get_db  # Import the get_db function
from flask_login import LoginManager
from mongoengine import connect
from flask_mongoengine import MongoEngine
from bson import ObjectId  # Import ObjectId from bson


DB_NAME = "my-proDB"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # Define the convert_to_object_id function
    def convert_to_object_id(value):
        try:
            # Attempt to convert the value to ObjectId
            object_id = ObjectId(value)
            return object_id
        except Exception as e:
            # Handle the exception or log it as needed
            print(f"Error converting '{value}' to ObjectId: {str(e)}")
            return None
        
    #Configure MongoDB connection
    app.config['MONGODB_SETTINGS'] = {
        'db': 'my-proDB',
        'host': 'mongodb+srv://antony313:hcXPkEGLdvMqxYIC@my-prodb.f72oapk.mongodb.net/',
    }
    # Initialize the MongoDB connection
    db = MongoEngine(app)
    # Initialize the MongoDB connection
    #connect(DB_NAME, host='mongodb://localhost:27017/')

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        try:
            object_id = ObjectId(id)
            return User.objects(id=object_id).first()
        except Exception as e:
            print(f"Error loading user by id: {str(e)}")
            return None


    return app


