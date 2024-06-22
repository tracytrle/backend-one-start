

# from flask import Flask, render_template, request, redirect, jsonify, url_for, session
# # from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from flask_cors import CORS
# from flask_session import Session
# from app import create_app, db
# from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, pipeline



# app = create_app()
# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)
# CORS(app)
# tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
# model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
# sentiment_classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)


# @app.route('/api/data', methods=['GET'])
# def get_data():

#     name = request.args.get('name')
#     input = request.args.get('input')

#     # Use default values if parameters are not provided
#     if name == 'roberta':
#         return redirect(url_for('get_roberta_result', input=input))
#     elif name == 'distilbert':
#         text = "I love this product! It's amazing."
#         return sentiment_classifier(text)
#     return f'Hello, {name}! You are {age} years old.'


# @app.route('/api/data', methods=['POST'])
# def post_data():
#     data = request.json
#     return jsonify(data), 201




# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5001)

# from . import create_app
from flask import Flask
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from .config import Config

# db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    # db.init_app(app)
    CORS(app)
    
    from routes.root_router import bp as root_bp
    app.register_blueprint(root_bp)
    
    from routes.roberta_router import bp as roberta_bp
    app.register_blueprint(roberta_bp)

    from routes.distilbert_router import bp as distilbert_bp
    app.register_blueprint(distilbert_bp)
    
    return app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

