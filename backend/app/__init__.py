# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # ✅ Import CORS
from dotenv import load_dotenv
import os
from app.models import db  # ✅ import shared instance

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # ✅ attach db instance to app

    # ✅ Enable CORS for all routes and allow requests from frontend
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    from app.routes.product_routes import product_bp
    app.register_blueprint(product_bp)

    return app
