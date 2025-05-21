from flask import Flask

app=Flask(__name__)


@app.route("/")
def index():
    return "Welcome to flask framework"


@app.route("/username")
def username():
    return "Hello Guvi"

@app.route("/contact")
def contact():
    return "Contact us"

@app.route("/user/<username>")
def showuser(username):
    return f'Hello{username}'

@app.route("/post/<int:_id>")
def postuser(_id):
    return f'Hello post{_id}'


@app.route("/path/<path:subpath>")
def showpath(subpath):
    return f'hello path is {subpath}'


