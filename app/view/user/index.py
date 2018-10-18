from flask import Blueprint, jsonify

user = Blueprint("user", __name__)


# 获取用户列表
@user.route("/users", methods=["GET"])
def users():
    return jsonify([{"name": "zsf"}])
