# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, HiddenField
from wtforms.validators import Email, DataRequired, EqualTo

# login and registration


class LoginForm(FlaskForm):
    username = TextField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = TextField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = TextField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])


class ForgotPasswordForm(FlaskForm):
    email = TextField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])


class ResetPasswordForm(FlaskForm):
    email_token_key = HiddenField()
    email = HiddenField()
    password = PasswordField('New Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    confirm_password = PasswordField(u'Confirm Password again',
                                     [EqualTo('password',
                                              message="Passwords don't match")])
