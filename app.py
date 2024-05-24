from flask import Flask, render_template, request, session, redirect, url_for, jsonify, send_from_directory
import os

app = Flask(__name__, template_folder='.')
app.secret_key = os.urandom(24)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/')
def login():
    return send_from_directory('.', 'login.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

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

        return redirect(url_for('dashboard'))
    else:
        return send_from_directory('.', 'register.html')

@app.route('/courses.html')
def courses():
    return send_from_directory('.', 'courses.html')

@app.route('/contact.html')
def contact():
    return send_from_directory('.', 'contact.html')

@app.route('/contact.html', methods=['POST'])
def contact_post():
    return redirect(url_for('courses'))

@app.route('/logout.html')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/enroll.html')
def enroll():
    return send_from_directory('.', 'enroll.html')

@app.route('/enroll.html', methods=['POST'])
def enroll_post():
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
