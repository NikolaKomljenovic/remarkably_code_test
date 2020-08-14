from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Remarkably Code Test',
    version='0.1.0',
    description='Backend API for Remarkably Code Test'
)