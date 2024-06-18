
# # /__init__.py
# from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from .config import Config

# # db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     # app.config.from_object(Config)
#     # db.init_app(app)
    
#     from .routes.roberta_router import bp as roberta_bp
#     app.register_blueprint(roberta_bp)
    
#     return app