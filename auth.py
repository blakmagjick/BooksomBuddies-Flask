from flask_login import current_user
from flask import jsonify

SUPERUSER = "sudo"

def can_update(id):
    return (current_user.id == id or current_user.username == SUPERUSER)

def unauthorized():
    return jsonify(
        data={},
        message="Unauthorized",
        status=403
    ), 403