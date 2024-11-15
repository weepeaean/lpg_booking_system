from flask_cors import CORS 
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lpg_bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Home route (login page as default)
@app.route('/')
def home():
    # Check if user is logged in
    if 'user' in session:
        # Redirect to dashboard if logged in
        return redirect(url_for('dashboard'))
    return render_template('home.html')  # Render home page if not logged in

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login_page'))  # If no session, redirect to login
    return render_template('dashboard.html')  # Render the dashboard page

# Booking page route
@app.route('/booking')
def booking():
    return render_template('booking.html')

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('username')  # Access the form data
        password = request.form.get('password')
        # Verify credentials
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user'] = user.id  # Set session variable on successful login
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    elif 'user' in session:
        return redirect(url_for('dashboard'))  # Redirect if already logged in
    return render_template('login.html')  # Default response for GET request

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Forgot password page route
@app.route('/forget')
def forget():
    return render_template('forget.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user session
    return redirect(url_for('home'))  # Redirect to home page after logout

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password_hash = generate_password_hash(password)  # Hash the password
        
        # Create a new user in the database
        new_user = User(username=username, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login_page'))  # Redirect to login after successful registration
    
    return render_template('register.html')  # Render the registration page for GET request

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully.")
    app.run(debug=True)
