from flask import Blueprint, redirect, url_for, request, jsonify
from service.distilbert_service import get_result

bp = Blueprint('distilbert_router', __name__)

@bp.route('/api/distilbert', methods=['GET'])
def analyze_text():
    input_text = request.args.get('input', "I wish I have a lot of money")
    sentences = [input_text]
    result = get_result(sentences)
    return jsonify(result)