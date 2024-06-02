from flask import Blueprint, request, jsonify
from .models import db, User

api_bp = Blueprint('api', __name__)

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not 'username' in data or not 'email' in data:
        return jsonify({'message': 'Invalid data'}), 400

    username = data['username']
    email = data['email']
    is_teacher = data.get('is_teacher', False)
    is_learner = data.get('is_learner', True)

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'User with this username already exists'}), 400

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'User with this email already exists'}), 400

    new_user = User(username=username, email=email, is_teacher=is_teacher, is_learner=is_learner)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201