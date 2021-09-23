# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_mailman import EmailMessage
from apps.config import Config

def send_email(subject, body, send_to):

    msg = EmailMessage(
        subject,
        body,
        Config.MAIL_USERNAME,
        [send_to]
    )
    msg.content_subtype = "html"
    msg.send()
