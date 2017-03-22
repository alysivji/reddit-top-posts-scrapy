#!/usr/bin/env python3

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField, URLField


class Post(Document):
    ''' Class for defining structure of reddit-top-posts collection
    '''
    url = URLField(required=True)
    date = DateTimeField(required=True)
    date_str = StringField(max_length=10, required=True)
    commentsUrl = URLField(required=True)
    sub = StringField(max_length=20, required=True) # subredit can be 20 chars
    title = StringField(max_length=300, required=True) # title can be 300 chars
    score = IntField(required=True)

    meta = {
        'collection': 'top_reddit_posts', # collection name
        'ordering': ['-score'], # default ordering
        'auto_create_index': False, # MongoEngine will not create index
        }
