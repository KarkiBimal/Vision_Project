from flask import Flask, render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegisterationForm, LoginForm, UpdateAccountForm
from application.models import User #fixing the circular import error.
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')   # control this and home page, no need to pass the title
@app.route('/Home')
def Home():
    return render_template('Home.html',title='Home') #rendering from home.html file

@app.route('/About')
def About():
    return render_template('About.html', title='About') #connecting another about.html file

@app.route('/register', methods=['GET', 'POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form=RegisterationForm()
    if form.validate_on_submit(): 
        hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Now, you can login.', 'success')
        return redirect(url_for('Login'))

        # flash('Cannot process your request with given credentials','danger')
    return render_template('Register.html', title='Register',form =form )

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page=request.args.get('next')
            flash('Your have successfully logged-in.','success')
            return redirect(next_page) if next_page else redirect(url_for('Home'))

        else:
            flash('Login Unsuccessfull. Please check your email and password', 'danger')
    return render_template('Login.html', title='Login',form =form )

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged-out successfully','success')
    return redirect(url_for('Home'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated successfully', 'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email

    return render_template('account.html', title='Account', form=form )
