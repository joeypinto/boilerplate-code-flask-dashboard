# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, FileField
from wtforms.validators import Email, DataRequired

# user profile


class ProfileForm(FlaskForm):
    firstname = TextField('First Name', id='first_name', validators=[DataRequired()])
    lastname = TextField('Last Name', id='last_name', validators=[DataRequired()])
    birthday = TextField('Birthday', id='birthday', validators=[DataRequired()])
    gender = SelectField('Gender', id='gender', choices=[("1", "Male"), ("2", "Female")])
    email = TextField('Email', id='email', validators=[DataRequired(), Email()])
    phone = TextField('Phone', id='phone', validators=[DataRequired()])
    address = TextField('Address', id='address', validators=[DataRequired()])
    number = TextField('Number', id='number', validators=[DataRequired()])
    city = TextField('City', id='city', validators=[DataRequired()])
    zipcode = TextField('Zip Code', id='zipcode', validators=[DataRequired()])
    photo = FileField('Profile Photo', id='photo', validators=[DataRequired()])
