from flask import Flask, request, redirect, render_template
import cgi #CGI code is invoked by an HTTP server, to process user submitted input through an HTML form.
import re  #using re library to verify email takes what I had in a longer loop and makes it simpler. Could also use this for password check and username.
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")#html form used to create page.
def index():
    return render_template('index.html')

@app.route("/", methods=['post'])
def submitted(): #User submitted information.
    username = request.form['username']
    password = request.form['password']
    passcheck = request.form['passcheck']
    email = request.form['email']
    username_error = ''    #Index Error
    password_error = ''
    passcheck_error = ''
    email_error = ''
    for un in username:   #Username check and verify loop, looks that there is not a empty field, space, and character count of 3-20 if dont meet the requirement error is shown.
            if un.isspace():
                username_error = 'Username cannot contain spaces.'
            elif (len(username) < 3) or (len(username) > 20):
                    username_error = 'Username needs to be 3-20 characters.'
    if not username:
            username_error = 'Not a valid username'
            username = ''
    if password == '':          #Password check and verify loop
        password_error = 'Must have a password'
        password = ''
    elif len(password) < 3 or len(password) > 20:
            password_error = 'Password length must be between 3-20 characters.'
            password = ''
    else:
        if password != passcheck:
            passcheck_error = "Passwords don't match."
            passcheck = ''
    if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):        #Email Check and verify loop.
            email_error = 'This is not a valid email, please check for space "@""." and length of 3-20 characters.'
            email = ''   #Redirects to welcome page or shows what your error is. 
    if (not username_error) and (not password_error) and (not passcheck_error) and (not email_error):
            return redirect('/welcome?name={0}'.format(username))

    return render_template('index.html', username=username, email=email,
                           username_error=username_error, password_error=password_error,
                           passcheck_error=passcheck_error, email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('name')
    return render_template('welcome.html', username = username)

app.run()
