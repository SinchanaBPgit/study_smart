from flask import Flask, send_from_directory, request, session, redirect, url_for
import os

app = Flask(_name_, template_folder='.')
app.secret_key = os.urandom(24)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check credentials here (add logic)
        return redirect(url_for('dashboard'))
    else:
        return send_from_directory('.', 'login.html')

@app.route('/dashboard')
def dashboard():
    return send_from_directory('.', 'dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # Register the user here (add logic)
        return redirect(url_for('dashboard'))
    else:
        return send_from_directory('.', 'register.html')

@app.route('/courses.html')
def courses():
    return send_from_directory('.', 'courses.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/contact.html', methods=['POST'])
def contact_post():
    # Handle form submission logic here
    return redirect(url_for('courses'))

@app.route('/logout.html')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/enroll.html', methods=['GET'])
def enroll():
    return send_from_directory('.', 'enroll.html')

@app.route('/enroll.html', methods=['POST'])
def enroll_post():
    # Handle enrollment logic here
    return redirect(url_for('dashboard'))

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

if __name__ == '__main__':
    app.run(debug=True)
