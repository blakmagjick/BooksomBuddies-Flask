import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

books = Blueprint('books', 'books')

#INDEX ROUTE
@books.route('/', methods=['GET'])
def books_index():
    result = models.Book.select()

    book_dicts = [model_to_dict(book) for book in result]

    current_user_book_dicts = [model_to_dict(book) for book in current_user.books]

    for book_dict in current_user_book_dicts:
        book_dict['owner'].pop('password')

    return jsonify (
        data=current_user_book_dicts,
        message=f"Successfully found {len(current_user_book_dicts)} books",
        status=200
    ), 200

#CREATE ROUTE
@books.route('/', methods=['POST'])
def create_book():
    payload = request.get_json()

    new_book = models.Book.create(**payload, owner=current_user.id)
    print(new_book)

    book_dict = model_to_dict(new_book)
    book_dict['owner'].pop('password')

    return jsonify (
        data=book_dict,
        message='Successfully added book',
        status=201
    ), 201

#SHOW ROUTE
@books.route('/<id>', methods=['GET'])
def show_one_book(id):
    book = models.Book.get_by_id(id)
    return jsonify (
        data=model_to_dict(book),
        message='*party emoji*',
        status=200
    ), 200

#UPDATE ROUTE
@books.route('/<id>', methods=['PUT'])
def update_book(id):
    payload = request.get_json()

    models.Book.update(**payload).where(models.Book.id == id).execute()

    return jsonify (
        data=model_to_dict(models.Book.get_by_id(id)),
        message='Book has been successfully updated',
        status= 200
    ), 200

#DELETE ROUTE