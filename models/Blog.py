"""
This model is for the blogs

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from mongoengine.fields import DateTimeField
import datetime

class Blog(Document):
    username = StringField(required=True)
    name = StringField(required=True)
    content = StringField(required=True)
    tags = ListField(StringField())
    date = DateTimeField(default=datetime.datetime.utcnow)
