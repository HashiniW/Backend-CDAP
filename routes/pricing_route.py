from flask import Flask
from flask import Blueprint
from flask_restful import Api

from resources.pricing_resource import GetVegiTiles 

pricing_blueprint = Blueprint('lstm', __name__)
pricing_blueprint_api = Api(pricing_blueprint)

pricing_blueprint_api.add_resource(
    GetVegiTiles, '/get-vegi-tiles', methods=['POST'])
