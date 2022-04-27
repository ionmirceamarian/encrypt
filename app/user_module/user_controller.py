from flask import Blueprint, request
from app.auth_tools import protected_endpoint
from .user_facade import UserFacade

user_controller = Blueprint("users", __name__, url_prefix="/")

@user_controller.route("/register", methods=["POST"])
def register_user():
    if request.method == 'POST':
        user = request.get_json()
        UserFacade.check_params(user)
        return UserFacade().create_user(user)

@user_controller.route("/login", methods=["POST"])
def login_user():
    if request.method == 'POST':
        user = request.get_json()
        UserFacade.check_params(user)
        return UserFacade().login_user(user)

@user_controller.route("/logout", methods=["GET"])
@protected_endpoint()
def logout_users():
    if request.method == 'GET':
        auth_token = request.headers.get("Authorization")
        return UserFacade().logout_user(auth_token)
