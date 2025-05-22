from flask import Flask , url_for
app=Flask(__name__)

@app.route('/')
def index():
    return"Welcome to flask framework"

@app.route("/login")
def loginUser():
    return f'login page'

@app.route("/user/<username>")
def user(username):
    return f'user page {username}'

with app.test_request_context():
    print(url_for('loginUser'))
    print(url_for('user',username="Naresh"))
    print(url_for('index'))