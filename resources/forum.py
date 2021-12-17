import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

from auth import can_update, unauthorized

posts = Blueprint('posts', 'posts')

#POST INDEX ROUTE
@posts.route('/', methods=['GET'])
@login_required
def post_index():
    result = models.Post.select()

    post_dicts = [model_to_dict(post) for post in result]

    for post_dict in post_dicts:
        post_dict['author'].pop('password')

    return jsonify (
        data=post_dicts,
        message=f"Successfully found {len(post_dicts)} posts",
        status=200
    ), 200

#POST CREATE ROUTE
@posts.route('/', methods=['POST'])
@login_required
def create_post():
    payload = request.get_json()
    print(payload)
    new_post = models.Post.create(**payload, author=current_user.id)

    post_dict = model_to_dict(new_post)
    post_dict['author'].pop('password')

    return jsonify (
        data=post_dict,
        message='Successfully created new post to book forum',
        status=201
    ), 201

#POST SHOW ROUTE
@posts.route('/<id>', methods=['GET'])
@login_required
def show_post(id):
    post = models.Post.get_by_id(id)
    return jsonify (
        data=model_to_dict(post),
        message='*party emoji*',
        status=200
    ), 200

#POST UPDATE ROUTE
@posts.route('/<id>', methods=['PUT'])
@login_required
def update_post(id):
    payload = request.get_json()

    post = models.Post.get_by_id(id)

    if not can_update(post.author.id):
        return unauthorized()

    models.Post.update(**payload).where(models.Post.id == id).execute()

    return jsonify (
        data=model_to_dict(models.Post.get_by_id(id)),
        message='Post has been updated',
        status=200
    ), 200

#POST DELETE ROUTE
@posts.route('/<id>', methods=['DELETE'])
@login_required
def delete_post(id):
   
    post = models.Post.get_by_id(id)

    if not can_update(post.author.id):
        return unauthorized()

    delete_post = models.Post.delete().where(models.Post.id == id).execute()

    return jsonify (
        data={},
        message=f"Successfully deleted post",
        status=200
    ), 200

#ALL COMMENTS
@posts.route('/comments/', methods=['GET'])
@login_required
def all_comments():
    result = models.Comment.select()

    comment_dicts = [model_to_dict(comment) for comment in result]

    for comment_dict in comment_dicts:
        comment_dict['postid']['author'].pop('password')
        comment_dict['author'].pop('password')
  
    return jsonify(
        data=comment_dicts,
        message=f"Found all comments",
        status=200
    ), 200

#COMMENT INDEX ROUTE
@posts.route('/comments/<post_id>', methods=['GET'])
@login_required
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
@login_required
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
@posts.route('/comments/<comment_id>', methods=['GET'])
@login_required
def show_comment(comment_id):
    comment = models.Comment.get_by_id(comment_id)
    return jsonify (
        data=model_to_dict(comment),
        message='*party emoji*',
        status=200
    ), 200

#COMMENT UPDATE ROUTE
@posts.route('/comments/<comment_id>', methods=['PUT'])
@login_required
def update_comment(comment_id):
    payload = request.get_json()

    models.Comment.update(**payload).where(models.Comment.id == comment_id).execute()

    updated_comment = model_to_dict(models.Comment.get_by_id(comment_id))
    updated_comment['postid']['author'].pop('password')
    updated_comment['author'].pop('password')

    return jsonify (
        data=updated_comment,
        message='Comment has been updated',
        status=200
    ), 200

#COMMENT DELETE ROUTE
@posts.route('/comments/<comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):

    comment_to_delete = models.Comment.delete().where(models.Comment.id == comment_id).execute()

    return jsonify (
        data={},
        message=f'Successfully deleted post',
        status=200
    ), 200