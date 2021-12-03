import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

posts = Blueprint('posts', 'posts')

#INDEX ROUTE
@posts.route('/', methods=['GET'])
def post_index():
    result = models.Post.select()

    post_dicts = [model_to_dict(post) for post in result]

    # current_user_post_dicts = [model_to_dict(post) for post in current_user.posts]

    # for post_dict in current_user_post_dicts:
    #     post_dict['name'].pop('password')
    
    return jsonify (
        data=post_dicts,
        message=f"Successfully found {len(post_dicts)} posts",
        status=200
    ), 200


#CREATE ROUTE
@posts.route('/', methods=['POST'])
def create_post():
    payload = request.get_json()

    new_post = models.Post.create(**payload, name=current_user.id)

    post_dict = model_to_dict(new_post)
    post_dict['name'].pop('password')

    return jsonify (
        data=post_dict,
        message="Successfully created new post to book forum",
        status=201
    ), 201

#SHOW ROUTE
@posts.route('/<id>', methods=['GET'])
def show_post(id):
    post = models.Post.get_by_id(id)
    return jsonify (
        data=model_to_dict(post),
        message='*party emoji*',
        status=200
    ), 200

#UPDATE ROUTE
@posts.route('/<id>', methods=['PUT'])
def update_post(id):
    payload = request.get_json()

    models.Post.update(name=current_user.id, **payload).where(models.Post.id == id).execute()

    return jsonify (
        data=model_to_dict(models.Post.get_by_id(id)),
        message='Post has been updated',
        status=200
    ), 200

#DELETE ROUTE
@posts.route('/<id>', methods=['DELETE'])
def delete_post(id):
    delete_post = models.Post.delete().where(models.Post.id == id).execute()

    return jsonify (
        data={},
        message=f"Successfully deleted post",
        status=200
    ), 200