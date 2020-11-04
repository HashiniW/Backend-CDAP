from flask_restful import Resource
from flask import request

class GetSuppliers(Resource):
    def post(self):
        data = request.get_json()
        data={"data":[{"NIC":"681285364V","name":"W.M.B.Sumanasiri","image":"https://i.ibb.co/qCqC9DH/a.png"},{"NIC":"885632479V","name":"S.P.Jayawardhane","image":"https://i.ibb.co/8g78vSH/b.png"},{"NIC":"635698741V","name":"H.D.N.Hemapala","image":"https://i.ibb.co/Rcc0jZ4/c.png"}],"success":'true'}
        return data

class GetBestFarmer(Resource):
    def post(self):
        data = request.get_json()
        # print(data)
        # return data['vegi_name']
        if data['vegi_name'] == 'carrot':
            return {"data":[{"date":"24/09/2020","demand":223,"vegName":"Carrot","supplierId":17},{"date":"23/09/2020","demand":323,"vegName":"Carrot","supplierId":15},{"date":"22/09/2020","demand":213,"vegName":"Carrot","supplierId":20},{"date":"21/09/2020","demand":300,"vegName":"Carrot","supplierId":18},{"date":"20/09/2020","demand":253,"vegName":"Carrot","supplierId":17},{"date":"19/09/2020","demand":263,"vegName":"Carrot","supplierId":16},{"date":"18/09/2020","demand":330,"vegName":"Carrot","supplierId":14},{"date":"17/09/2020","demand":200,"vegName":"Carrot","supplierId":15},{"date":"16/09/2020","demand":250,"vegName":"Carrot","supplierId":17},{"date":"15/09/2020","demand":215,"vegName":"Carrot","supplierId":13}],"success":'true'}
        else:
            return {"data":[{"date":"24/09/2020","demand":323,"vegName":"Pumpkin","supplierId":18},{"date":"23/09/2020","demand":333,"vegName":"Pumpkin","supplierId":20},{"date":"22/09/2020","demand":213,"vegName":"Pumpkin","supplierId":12},{"date":"21/09/2020","demand":340,"vegName":"Pumpkin","supplierId":19},{"date":"20/09/2020","demand":370,"vegName":"Pumpkin","supplierId":14},{"date":"19/09/2020","demand":370,"vegName":"Pumpkin","supplierId":18},{"date":"18/09/2020","demand":210,"vegName":"Pumpkin","supplierId":16},{"date":"17/09/2020","demand":380,"vegName":"Pumpkin","supplierId":13},{"date":"16/09/2020","demand":380,"vegName":"Pumpkin","supplierId":12},{"date":"15/09/2020","demand":310,"vegName":"Pumpkin","supplierId":17}],"success":'true'}