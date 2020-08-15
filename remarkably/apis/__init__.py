from flask import Blueprint
from flask_restplus import Api
from rest.event import api as event

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Remarkably Code Test',
    version='0.1.0',
    description='Backend API for Remarkably Code Test'
)

api.add_namespace(event, path="/event")
