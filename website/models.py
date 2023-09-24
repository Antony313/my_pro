from mongoengine import Document, StringField, DateTimeField, ReferenceField
from flask_login import UserMixin
from datetime import datetime

class Note(Document):
    data = StringField(max_length=10000)
    date = DateTimeField(default=datetime.utcnow)
    user = ReferenceField('User')

class User(Document, UserMixin):
    email = StringField(max_length=150, unique=True)
    password = StringField(max_length=150)
    first_name = StringField(max_length=150)
