"""
This model is for the blogs

"""

import datetime

from mongoengine import Document, StringField, ListField
from mongoengine.fields import DateTimeField


class Blog(Document):
    username = StringField(required=True)
    name = StringField(required=True)
    content = StringField(required=True)
    tags = ListField(StringField())
    date = DateTimeField(default=datetime.datetime.utcnow)
