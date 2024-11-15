# Import necessary functions
from werkzeug.security import generate_password_hash

# Hash the existing plain text passwords
testuser_password = generate_password_hash('testpass')
existing_user_password = generate_password_hash('password123')
new_user_password = generate_password_hash('new_password')

# Print the hashed passwords to see the output
print(f"testuser hashed password: {testuser_password}")
print(f"existing_user hashed password: {existing_user_password}")
print(f"new_user hashed password: {new_user_password}")
