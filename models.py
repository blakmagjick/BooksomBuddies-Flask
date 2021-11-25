from peewee import *
import datetime

from flask_login import UserMixin

DB = SqliteDatabase('booksom.sqlite')

class BaseModel(Model):
    class Meta:
        database = DB

class User(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

class Book(BaseModel):
    title = CharField(unique=True)
    author =  CharField()
    cover = CharField()
    genre = CharField()
    notes = CharField()
    owner = ForeignKeyField(User, backref='books')

class Post(BaseModel):
    name = ForeignKeyField(User, backref='posts')
    post = CharField()
    comment = CharField()
    date = DateTimeField(default=datetime.datetime.now)

def initialize():
    DB.connect()
    DB.create_tables([User, Book, Post], safe=True)
    DB.close()