import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

posts = Blueprint('posts', 'posts')

#POST INDEX ROUTE
@posts.route('/', methods=['GET'])
def post_index():
    result = models.Post.select()

    post_dicts = [model_to_dict(post) for post in result]

    return jsonify (
        data=post_dicts,
        message=f"Successfully found {len(post_dicts)} posts",
        status=200
    ), 200

#POST CREATE ROUTE
@posts.route('/', methods=['POST'])
def create_post():
    payload = request.get_json()

    new_post = models.Post.create(**payload, author=current_user.id)

    post_dict = model_to_dict(new_post)
    post_dict['author'].pop('password')

    return jsonify (
        data=post_dict,
        message="Successfully created new post to book forum",
        status=201
    ), 201

#POST SHOW ROUTE
@posts.route('/<id>', methods=['GET'])
def show_post(id):
    post = models.Post.get_by_id(id)
    return jsonify (
        data=model_to_dict(post),
        message='*party emoji*',
        status=200
    ), 200

#POST UPDATE ROUTE
@posts.route('/<id>', methods=['PUT'])
def update_post(id):
    payload = request.get_json()

    models.Post.update(author=current_user.id, **payload).where(models.Post.id == id).execute()

    return jsonify (
        data=model_to_dict(models.Post.get_by_id(id)),
        message='Post has been updated',
        status=200
    ), 200

#POST DELETE ROUTE
@posts.route('/<id>', methods=['DELETE'])
def delete_post(id):
    delete_post = models.Post.delete().where(models.Post.id == id).execute()

    return jsonify (
        data={},
        message=f"Successfully deleted post",
        status=200
    ), 200

#COMMENT INDEX ROUTE
@posts.route('/comments/<post_id>', methods=['GET'])
def get_comments(post_id):
    result = models.Comment.select()

    comment_dicts = [model_to_dict(comment) for comment in result]

    for comment_dict in comment_dicts:
        comment_dict['postid']['author'].pop('password')
        comment_dict['author'].pop('password')
  

    return jsonify(
        data=comment_dicts,
        message=f"Found comments",
        status=200
    ), 200

#COMMENT CREATE ROUTE
@posts.route('/comments/<post_id>', methods=['POST'])
def create_comment(post_id):
    payload = request.get_json()

    new_comment = models.Comment.create(**payload, author=current_user.id, postid=post_id)

    comment_dict = model_to_dict(new_comment)
    comment_dict['postid']['author'].pop('password')
    comment_dict['author'].pop('password')

    return jsonify (
        data=comment_dict,
        message='Successfully created comment',
        status=201
    ), 201

#COMMENT SHOW ROUTE