from peewee import *
import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('booksom.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Book(Model):
    title = CharField(unique=True)
    author =  CharField()
    series = CharField()
    cover = CharField()
    genre = CharField()
    notes = CharField()
    owner = ForeignKeyField(User, backref='books')

    class Meta:
        database = DATABASE

class Post(Model):
    name = ForeignKeyField(User, backref='posts')
    post = CharField()
    comment = CharField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Book, Post], safe=True)
    DATABASE.close()