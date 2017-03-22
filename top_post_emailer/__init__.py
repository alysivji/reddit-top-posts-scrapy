#!/usr/bin/env python3

import os
import configparser
from mongoengine.connection import connect
from .data_model import Post
from .render_template import render
from .mailgun_emailer import send_email

def email_last_scraped_date():
    ## mongodb params (using configparser)
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'settings.cfg'))
    mlab_uri = config.get('MongoDB', 'mlab_uri')

    # connect to db
    MONGO_URI = mlab_uri
    connect('sivji-sandbox', host=MONGO_URI)    

    ## get the last date the webscraper was run
    for post in Post.objects().fields(date_str=1).order_by('-date_str').limit(1):
        day_to_pull = post.date_str

    ## pass in variables, render template, and send
    context = {
        'day_to_pull': day_to_pull,
        'Post': Post,
    }
    html = render("template.html", context)
    send_email(html)
