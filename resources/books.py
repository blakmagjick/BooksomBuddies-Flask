import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

books = Blueprint('books', 'books')

@books.route('/', methods=['GET'])
def books_index():
    result = models.Book.select()

    book_dicts = [model_to_dict(book) for book in result]

    current_user_book_dicts = [model_to_dict(book) for book in current_user.books]

    for book_dict in current_user_book_dicts:
        book_dict['owner'].pop('password')

    return jsonify (
        data=current_user_book_dicts,
        message=f"Successfully found {len(current_user_book_dict)} books",
        status=200
    ), 200