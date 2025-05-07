from flask import Flask
from app.model.loader import load_model_and_vectorizer

def create_app():
    app = Flask(__name__)

    # Load model/vectorizer
    app.model, app.vectorizer = load_model_and_vectorizer()

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
