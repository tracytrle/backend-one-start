from flask import request, jsonify
from service.roberta_service import get_result

def analyze_text():
    input_text = request.args.get('input', "I wish I have a lot of money")
    sentences = [input_text]
    result = get_result(sentences)
    return jsonify(result)