from app import app, bcrypt, db
from flask import render_template, flash
from app.models import User
from app.forms import RegisterForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): # 當前端提交後的東西獲取與處理
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        # print(username, email, password)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, registration success', category='success')
    return render_template('register.html', form=form)