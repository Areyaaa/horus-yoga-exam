from app.models.user import User
from app.extensions import db
from app.utils.validators import validate_user_input

class UserService:
    @staticmethod
    def create_user(data):
        errors = validate_user_input(data)
        if errors:
            return {'success': False, 'errors': errors}
        
        try:
            user = User(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                nama=data['nama']
            )
            db.session.add(user)
            db.session.commit()
            return {'success': True, 'user': user.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'errors': [str(e)]}

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
        
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def update_user(user_id, data):
        errors = validate_user_input(data, for_update=True)
        if errors:
            return {'success': False, 'errors': errors}
        
        try:
            user = User.query.get(user_id)
            if not user:
                return {'success': False, 'errors': ['User not found']}
            
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.nama = data.get('nama', user.nama)
            if 'password' in data and data['password']:
                user.password = data['password']
            
            db.session.commit()
            return {'success': True, 'user': user.to_dict()}
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'errors': [str(e)]}

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return {'success': False, 'errors': ['User not found']}
            
            db.session.delete(user)
            db.session.commit()
            return {'success': True}
        except Exception as e:
            db.session.rollback()
            return {'success': False, 'errors': [str(e)]}