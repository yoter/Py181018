from flask import Blueprint, jsonify

user = Blueprint("user", __name__)


@user.route("/users", methods=["GET"])
def users():
    return jsonify([{"name": "zsf"}])
