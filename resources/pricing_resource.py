from flask_restful import Resource
from flask import request


class GetVegiTiles(Resource):
    def post(self):
        data = request.get_json()
        data = {"data": [{"name": "Carrot", "value": "Rs. 322.00"}, {"name": "Lettuce", "value": "Rs. 265.00"}, {"name": "Potato", "value": "Rs. 120.00"}, {"name": "Brinjal", "value": "Rs. 127.00"}, {"name": "Tomato", "value": "Rs. 243.00"}, {"name": "Beans", "value": "Rs. 400.00"}, {
            "name": "Garlic", "value": "Rs. 270.00"}, {"name": "Pumpkin", "value": "Rs. 205.00"}, {"name": "Cabbage", "value": "Rs. 202.00"}, {"name": "Cucumber", "value": "Rs. 102.00"}, {"name": "Cauliflower", "value": "Rs. 553.00"}, {"name": "Lime", "value": "Rs. 197.00"}], "success": 'true'}
        return data
