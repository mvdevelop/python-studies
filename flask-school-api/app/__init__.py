
from flask import Flask
from .routes.student_routes import student_bp

def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = 'uploads'

    app.register_blueprint(student_bp)

    return app
