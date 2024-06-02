from flask import Blueprint, jsonify, request
from .models import db, User
from .services.data_service import fetch_data
from .services.ml_service import perform_ml_task
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    data = fetch_data()
    return jsonify(data)

@api.route('/ml', methods=['POST'])
def ml_task():
    result = perform_ml_task()
    return jsonify(result)


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    print(f"Received data: username={username}, email={email}, password={password}")  # Debugging

    if not username or not email or not password:
        print("Missing username, email, or password")  # Debugging
        return jsonify({"error": "Username, email, and password are required"}), 400

    try:
        user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Error during registration: {e}")  # Debugging
        return jsonify({"error": "An error occurred during registration"}), 500

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if check_password_hash(user.password, password) and user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
