from flask import Blueprint
from controllers.roberta_controller import analyze_text

bp = Blueprint('roberta_router', __name__)

@bp.route('/api/roberta', methods=['GET'])
def get_roberta_result():
    return "analyze_text()"