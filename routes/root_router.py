from flask import Blueprint, redirect, url_for, request, jsonify
from service.distilbert_service import get_result

bp = Blueprint('root_router', __name__)

@bp.route('/', methods=['GET'])
def greeting():
    return "Hello, World!"