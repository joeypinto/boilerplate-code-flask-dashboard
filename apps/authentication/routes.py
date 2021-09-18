# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from uuid import uuid4

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import (LoginForm, CreateAccountForm,
                                       ForgotPasswordForm, ResetPasswordForm)
from apps.authentication.models import Users

from apps.authentication.util import verify_pass, hash_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))


# Login & Registration

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']

        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template('accounts/register.html',
                               msg='User created please <a href="/login">login</a>',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    forgot_password_form = ForgotPasswordForm(request.form)
    if 'forgot-password' in request.form:

        # read form data
        email = request.form['email']

        # Locate user
        user = Users.query.filter_by(email=email).first()

        # Check user exists
        if user:

            user.email_token_key = str(uuid4())
            db.session.add(user)
            db.session.commit()

            # create a set_password link to send in email
            email_url = url_for('authentication_blueprint.reset_password',
                                email=user.email,
                                email_token_key=user.email_token_key,
                                _external=True)
            print(email_url)  # todo: send email

            return render_template('registration/forgot_password.html',
                                   msg='Instructions sent successfully on your email <br> link is: ' + email_url,
                                   success=True,
                                   form=forgot_password_form)

        return render_template('registration/forgot_password.html',
                               msg='No user exists with this email',
                               success=False,
                               form=forgot_password_form)

    return render_template('registration/forgot_password.html', form=forgot_password_form)


def update_password(email, email_token_key, password):
    user = Users.query.filter_by(email_token_key=email_token_key, email=email).first()
    user.password = hash_pass(password)
    user.email_token_key = None
    db.session.add(user)
    db.session.commit()


@blueprint.route('/reset-password', methods=['GET', 'POST'])
def reset_password():

    reset_password_form = ResetPasswordForm(email_token_key=request.values["email_token_key"],
                                            email=request.values["email"])

    if 'reset-password' in request.form:
        update_password(reset_password_form.email.data,
                        reset_password_form.email_token_key.data,
                        reset_password_form.password.data)
        return redirect(url_for("authentication_blueprint.login", msg="Your password has been changed, log in again"))

    return render_template("registration/reset_password.html", form=reset_password_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))


# Errors

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
