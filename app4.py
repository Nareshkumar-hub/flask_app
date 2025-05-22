from flask import Flask , render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("pass1")
        return f'Email is {email} \n Password is {password}'

    print("i am just returning login page ")
    return render_template('login.html')    
