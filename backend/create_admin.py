from app import create_app, db
from app.models.user import User
from app.config import Config

def create_admin_user():
    app = create_app(Config)
    
    with app.app_context():
        # Check if admin already exists
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            # Create admin user
            admin = User(
                username='admin',
                password='Admin123',  # This will be hashed automatically
                email='admin@example.com',
                nama='Administrator'
            )
            
            db.session.add(admin)
            db.session.commit()
            print("Admin user created successfully!")
            print("Username: admin")
            print("Password: Admin123")
        else:
            print("Admin user already exists!")

if __name__ == '__main__':
    create_admin_user()