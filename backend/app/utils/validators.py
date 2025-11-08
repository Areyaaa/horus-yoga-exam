from email_validator import validate_email, EmailNotValidError

def validate_user_input(data, for_update=False):
    errors = []
    required_fields = ['username', 'email', 'nama']
    if not for_update:
        required_fields.append('password')
    
    # Check required fields
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"{field} is required")
    
    # Validate email format
    if 'email' in data and data['email']:
        try:
            validate_email(data['email'])
        except EmailNotValidError:
            errors.append("Invalid email format")
    
    # Validate password length if present
    if 'password' in data and data['password']:
        if len(data['password']) < 6:
            errors.append("Password must be at least 6 characters long")
    
    return errors