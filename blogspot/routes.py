from flask import render_template, url_for, flash, redirect 
from blogspot import app, db, bcrypt
from blogspot.forms import RegistrationForm, LoginForm
from blogspot.models import User, Post

posts=[
    {
        'author': 'Alex Queen',
        'title' :'Post 1',
        'content' : 'first post by Alex',
        'date_posted' :'Dec 17,2023'
    },
    {
        'author': 'Sera Queen',
        'title' :'Post 2',
        'content' : 'first post by Sera',
        'date_posted' :'Dec 18,2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts= posts)

@app.route("/about")
def about():
    return render_template("about.html", title= "About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username =form.username.data, email =form.email.data, password =hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created!, you are able to log in now', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title= 'Register', form= form)

@app.route("/login", methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful,Please check your email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title= 'Login', form= form)
