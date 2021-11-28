# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import random

from flask_migrate import Migrate
from sys import exit
from decouple import config

from apps.config import config_dict
from apps.home.models import Data
from apps import create_app, db

from sqlalchemy.orm.mapper import configure_mappers

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

@app.cli.command("reset_datatables")
def reset_datatables():
    """Reset and Init database with new sample in 'data' model."""

    db.drop_all()
    configure_mappers()
    db.create_all()

    for i in range(1, 100):
        _data = Data(type=random.choice(['product', 'transaction']),
                     name="name " + str(i),
                     value=random.randint(10, 100))
        db.session.add(_data)

    db.session.commit()
