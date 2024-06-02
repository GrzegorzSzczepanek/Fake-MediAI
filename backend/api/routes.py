from flask import Blueprint, jsonify
from .models import db, User
from .services.data_service import fetch_data
from .services.ml_service import perform_ml_task

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    data = fetch_data()
    return jsonify(data)

@api.route('/ml', methods=['POST'])
def ml_task():
    result = perform_ml_task()
    return jsonify(result)
