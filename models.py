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
    isbn = CharField()
    notes = CharField()
    owner = ForeignKeyField(User, backref='books')

class UserProfile(BaseModel):
    username = ForeignKeyField(User, backref='user')
    profilepic = CharField()
    name = CharField()
    location = CharField()
    # favebook = ForeignKeyField(Book, backref='user')
    favebook = CharField()
    wishlist = CharField()

class Post(BaseModel):
    title = CharField()
    author = ForeignKeyField(User, backref='posts')
    post = CharField()
    date = DateTimeField(default=datetime.datetime.now)

class Comment(BaseModel):
    comment = CharField()
    author = ForeignKeyField(User, backref='comments')
    postid = ForeignKeyField(Post, backref='comments')
    date = DateTimeField(default=datetime.datetime.now)

def initialize():
    DB.connect()
    DB.create_tables([User, Book, Post, Comment, UserProfile], safe=True)
    DB.close()