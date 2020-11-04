from flask import Flask
from flask import Blueprint
from flask_restful import Api

from resources.suplier_resource import GetSuppliers
from resources.suplier_resource import GetBestFarmer

suplier_blueprint = Blueprint('lstm', __name__)
suplier_blueprint_api = Api(suplier_blueprint)

suplier_blueprint_api.add_resource(GetSuppliers, '/get-suplier-list', methods = ['POST'])
suplier_blueprint_api.add_resource(GetBestFarmer, '/get-best-farmer', methods = ['POST'])
