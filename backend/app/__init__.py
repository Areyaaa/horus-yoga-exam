from flask import Flask, send_from_directory, jsonify, request
from app.extensions import db, migrate, bcrypt, cors
from app.config import Config
from app.routes import users
import os

def create_app(config_class=Config):
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
    app = Flask(__name__, 
                static_folder=static_folder,
                static_url_path='')
    
    # Load configuration
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(users.bp, url_prefix='/api/users')

    # Serve frontend
    @app.route('/')
    def serve_frontend():
        try:
            return send_from_directory(app.static_folder, 'login.html')
        except Exception as e:
            app.logger.error(f"Error serving frontend: {str(e)}")
            return jsonify(error="Internal server error"), 500

    @app.route('/<path:filename>')
    def serve_static(filename):
        try:
            return send_from_directory(app.static_folder, filename)
        except Exception as e:
            app.logger.error(f"Error serving static file {filename}: {str(e)}")
            return jsonify(error="File not found"), 404

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        if request.path.startswith('/api/'):
            return jsonify(error='Not Found'), 404
        return send_from_directory(app.static_folder, 'login.html')

    return app