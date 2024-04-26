from flask import render_template, redirect, flash, url_for
from app.account import account
from app.account.forms import LoginForm, RegistrationForm
from app import db
from app.account.models import User


@account.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
        flash('Username already exists!')
    return render_template('register.html', title='Register', form=form)


@account.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect(url_for('blog.posts'))
    return render_template('login.html', title='Sign In', form=form)


