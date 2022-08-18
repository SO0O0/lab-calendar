from flask import Blueprint
from flask_restful import Api, Resource
from models import get_all

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Register(Resource):
    def get(self):
        return [{'name': i.name, 'intime': i.intime, 'outtime': i.outtime, 'comment': i.comment} for i in get_all()]

api = Api(api_bp)
api.add_resource(Register, '/register')