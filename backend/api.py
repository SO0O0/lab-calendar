from flask import Blueprint
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, url_prefix='/api')

class Register(Resource):
    def get(self):
        return {'id': 1125, 'name': 'Noriko'}

api = Api(api_bp)
api.add_resource(Register, '/register')