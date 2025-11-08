from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
import jwt
from datetime import datetime, timedelta
from functools import wraps
from app.config import Config

bp = Blueprint('users', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            token = token.split()[1]  # Remove 'Bearer' prefix
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['user_id']
        except:
            return jsonify({'message': 'Invalid token'}), 401
        return f(current_user_id, *args, **kwargs)
    return decorated

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    result = UserService.create_user(data)
    if result['success']:
        return jsonify(result['user']), 201
    return jsonify({'errors': result['errors']}), 400

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = UserService.get_user_by_username(data.get('username'))
    
    if user and user.check_password(data.get('password')):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + Config.JWT_ACCESS_TOKEN_EXPIRES
        }, Config.JWT_SECRET_KEY)
        return jsonify({
            'token': token,
            'user': user.to_dict()
        })
    
    return jsonify({'message': 'Invalid credentials'}), 401

@bp.route('/<int:user_id>', methods=['GET'])
@token_required
def get_user(current_user_id, user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.to_dict())

@bp.route('', methods=['GET'])
@token_required
def get_users(current_user_id):
    users = UserService.get_all_users()
    return jsonify(users)

@bp.route('/<int:user_id>', methods=['PUT'])
@token_required
def update_user(current_user_id, user_id):
    if int(current_user_id) != int(user_id):
        return jsonify({'message': 'Unauthorized'}), 403
    
    data = request.json
    result = UserService.update_user(user_id, data)
    if result['success']:
        return jsonify(result['user'])
    return jsonify({'errors': result['errors']}), 400

@bp.route('/<int:user_id>', methods=['DELETE'])
@token_required
def delete_user(current_user_id, user_id):
    if int(current_user_id) != int(user_id):
        return jsonify({'message': 'Unauthorized'}), 403
    
    result = UserService.delete_user(user_id)
    if result['success']:
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'errors': result['errors']}), 400