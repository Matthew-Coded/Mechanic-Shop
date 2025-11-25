from flask import Flask
from .extensions import db, ma
from .models import *
from .blueprints.customer import customer_bp
from flask_swagger_ui import get_swaggerui_blueprint # Needed to create a blueprint to plug into our app


SWAGGER_URL = "/api/docs" # URL for exposing my swagger ui
API_URL = "/static/swagger.yaml"

# Creating swagger blueprint
swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config = {"app_name": "Mechanic Shop API"})


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mechanic_shop.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(customer_bp, url_prefix="/customers")
    
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

    return app