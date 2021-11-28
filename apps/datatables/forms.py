# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, SelectField, FileField
from wtforms.validators import Email, DataRequired


class DatatableForm(FlaskForm):
    type   = SelectField('Type', id='type', choices=[("product", "Product"), ("transaction", "Transaction")], render_kw={'class':'form-select type'})
    name   = TextField('Name', id='name', validators=[DataRequired()], render_kw={'class':'form-control name'})
    value  = TextField('Value', id='value', validators=[DataRequired()], render_kw={'class':'form-control value'})