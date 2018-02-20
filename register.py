from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[aA-zZ\s]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process',methods=['POST','GET'])
def process():
    if len(request.form['email'])==0:
        flash("this form cant be left empty")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("this is not a valid email try again")
    if len(request.form['first_name'])==0:
        flash('this form cant be left empty')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("The name field cannot contain numbers")
    if len(request.form['last_name'])==0:
        flash('this form cant be left empty')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("This field cannot contain numbers")
    if len(request.form['password'])==0:
        flash('this form cant be left empty')
    if len(request.form['c_password'])==0:
        flash('this form cant be left empty')
    
    return render_template('complete.html',context={
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":request.form['password'],
        "c_password":request.form['c_password']
        })

app.run(debug=True)