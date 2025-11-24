from flask import Flask
from .extensions import db, ma
from .models import *
from .blueprints.customer import customer_bp



def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mechanic_shop.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(customer_bp, url_prefix="/customers")

    return app