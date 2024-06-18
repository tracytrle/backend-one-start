from flask import Flask, render_template, request, redirect, jsonify, url_for, session
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask_session import Session
from models.models import sentiment_classifier, classifier

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify(data), 201




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)