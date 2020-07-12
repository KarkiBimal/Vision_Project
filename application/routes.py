from flask import Flask, render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegisterationForm, LoginForm, UpdateAccountForm, Transcriptform
from application.models import User, Transcript #fixing the circular import error.
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')   # control this and home page, no need to pass the title

@app.route('/Home', methods=['GET', 'POST'])
def Home():
    
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
    return render_template('Home.html',title='Home',form=form) #rendering from home.html file

    

    

@app.route('/Videos', methods=['GET', 'POST'])
@login_required
def About():
   form=Transcriptform()
   if form.validate_on_submit(): 
    transcript=Transcript(transcript1=form.transcript1.data,transcript2=form.transcript2.data,transcript3=form.transcript3.data )
    db.session.add(transcript)
    db.session.commit()
   
   return render_template('Videos.html', title='About', form=form) #connecting another about.html file

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
        return redirect(url_for('/Videos'))
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

