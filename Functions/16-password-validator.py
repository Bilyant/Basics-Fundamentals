def password_validator(password: str):
    is_Valid = True
    errors = []

    if len(password) < 6 or len(password) > 10:
        is_Valid = False
        errors.append('Password must be between 6 and 10 characters')

    elif not password.isalnum():
        is_Valid = False
        errors.append('Password must consist only of letters and digits')

    digits_count = [n for n in password if n.isdigit()]
    if len(digits_count) < 2:
        is_Valid = False
        errors.append('Password must have at least 2 digits')

    if is_Valid:
        return 'Password is valid'
    else:
        return '\n'.join(errors)


password = input()
print(password_validator(password))
