from flask_restful import Resource
from predictions.lstm_price_model import LstmModel
from flask import request

class Predict(Resource):
    def get_tomato(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().get_tomato_prediction(data["Date"], data["Centre_Name"])
        return prediction

    def get_potato(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().get_potato_prediction(data["Date"], data["Centre_Name"])
        return prediction

    def get_onion(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().get_onion_prediction(data["Date"], data["Centre_Name"])
        return prediction

    def get_cabbage(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().get_cabbage_prediction(data["Date"], data["Centre_Name"])
        return prediction

    def get_brinjal(self):
        data = request.get_json()
       # print(data['Date'])
        #print('lstm')
        prediction = LstmModel().get_brinjal_prediction(data["Date"], data["Centre_Name"])
        return prediction
