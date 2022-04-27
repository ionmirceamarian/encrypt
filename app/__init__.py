from flask import Flask, make_response
from flask_migrate import Migrate
from sqlalchemy.sql import text
from app.license_module.license_controller import license_controller
from app.user_module.user_controller import user_controller
from app.config import Config
from app.extensions import db
import os

app = Flask(__name__)
os.environ["AUTH_SECRET"] = '28efc14a-1c9b-45e8-bb8b-2ad7fe6feb2c'


def config_app(app):
    app.config.from_object(Config())
    db.init_app(app)
    app.register_blueprint(license_controller)
    app.register_blueprint(user_controller)

def migrate_app(app):
    migrate = Migrate()
    migrate.init_app(app, db)

def main():
    config_app(app)
    migrate_app(app)

main()


@app.route("/status")
def health_check():
    try:
        db.session.query("1").from_statement(text("SELECT 1")).all()
        return make_response({"status": "OK"}, 200)
    except Exception as e:
        return make_response({"status": "Server Unavailable", "exception": str(e)}, 503)
