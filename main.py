from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['post'])
def submitted(): #User submitted information.
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
	#Index Error
    password_error = ''
    verify_error = ''
    email_error = ''
   #Username check
    if username =="":
        username_error = 'Must have a username!'
        username = ''
    elif len(username) > 20 or len(username) < 3:
        username_error = 'Username length must be between 3-20 characters.'
        username = ''
    #Password check and verify loop
    if password == '':
        password_error = 'Must have a password'
        password = ''
        if len(password) > 20 or len(password) < 3:
            password_error = 'Password length must be between 3-20 characters.'
            password = ''
    else:
        if password != verify:
            verify_error = "Passwords don't match."
            verify = ''
    #Email Check and verify loop.
    if email:
        if ("@") not in email:
            email_error = 'email must have @!'
        elif (".") not in email:
            email_error = 'must have a period!'
        elif " " in email:
            email_error = "Emails do not have spaces!"
        elif len(email) <= 3 or len(email) > 20:
            email_error = "email to short"
    if not password_error and not verify_error and not username_error and not email_error:
    #Redirects to welcome page or shows what your error is. 
        return redirect("/welcome?name={0}".format(username))
    else:
        return render_template('index.html', username_error=username_error,
            password_error=password_error, verify_error=verify_error, email_error = email_error, 
            username=username,
            password=password, email=email)

@app.route('/welcome')
def welcome():
    username = request.args.get('name')
    return render_template('welcome.html', username = username)

app.run()