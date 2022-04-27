from flask import jsonify, abort, make_response
import hashlib
from .user_models import User
from app.extensions import db
from app.logging import logger as log
from app.utils import (
    gen_salt,
    validate_email,
    NULL_PARAMS,
    INVALID_FORMAT
)
from app.auth_tools import (
    encode_auth_token,
    active_tokens
)

class UserFacade:
    def create_user(self, user):
        email = user.get("email")
        password = user.get("password")
        salt = gen_salt()
        hashed_pass = hashlib.sha256(
            f"{password}{salt}".encode("utf-8")
        ).hexdigest()
        current_user_info = self.get_user(email)

        if current_user_info is None:
            try:
                newUser = User(
                    email=email,
                )
                newUser.set_password(password)
                newUser.save()
                return {"status": True, "error": ""}
            except Exception as e:
                log.info('Failed to add user')
                log.exception(e)
        else:
            return {"error": "User already exists!"}
    
    def login_user(self, user):
        email = user.get("email")
        password = user.get("password")
        user_info = self.get_user(email)

        if user_info:
            if user_info.check_password(password=password):
                token = encode_auth_token(email)
                active_tokens.append(token)
                return {"auth_token": token}
            else:
                return {"error": "Password is incorrect."}
        else:
            return {"error": "User does not exist!"}
    
    def logout_user(self, auth_token):
        token_index = active_tokens.index(auth_token)
        del active_tokens[token_index]
        return {"status": 'Logged out successfully.'}
    
    @staticmethod
    def get_user(email):
        if not email:
            return {}
        else:
            return User.query.filter_by(email=email).first()

    @staticmethod
    def check_params(user):
        email = user.get("email")
        password = user.get("password")
        if (
            user is None
            or email is None
            or password is None
        ):
            abort(make_response(jsonify(error=NULL_PARAMS), 400))
       
        if (
            not validate_email(user.get("email"))
            or password is None
        ):
            abort(make_response(jsonify(error=INVALID_FORMAT), 400))
