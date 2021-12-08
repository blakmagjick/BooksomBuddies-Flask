import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

comments = Blueprint('comments', 'comments')

#SHOW ROUTE
@comments.route('/<id>', methods=['GET'])
def show_comment(id):
    comment = models.Comment.get_by_id(id)
    return jsonify (
        data=model_to_dict(comment),
        message='*party emoji*',
        status=200
    ), 200

#UPDATE ROUTE
@comments.route('/<id>', methods=['PUT'])
def update_comment(id):
    payload = request.get_json()

    models.Comment.update(**payload, name=current_user.id).where(models.Comment.id == id).execute()

    return jsonify (
        data=model_to_dict(models.Comment.get_by_id(id)),
        message='Comment has been udpated',
        status=200
    ), 200

#DELETE ROUTE
@comments.route('/<id>', methods=['DELETE'])
def delete_comment(id):
    delete_comment = models.Comment.delete().where(models.Comment.id == id).execute()

    return jsonify (
        data={},
        message=f'Successfully deleted post',
        status=200
    ), 200