# from werkzeug.security import generate_password_hash, check_password_hash
# from flask import request, jsonify
# # from flask import json
import pandas as pd
# import numpy as np
import pickle
import keras
# import json

from flask import jsonify

class LstmModel:

    def get_tomato_prediction(self, Date, Centre_Name):
        Data = pd.read_csv('lstm_price_prediction_tomato.csv')
        # result = Data.loc[(Data['Centre_Name'] == Centre_Name & (Data['Date'] == Date), 'Predicted_Retail_Price'].values
        result = {
            'Predicted_Retail_Price': Data.loc[(Data['Date'] == Date) & (Data['Centre_Name'] == Centre_Name), 'Predicted_Retail_Price'].values[0]}
        return jsonify(result)

    def get_potato_prediction(self, Date, Centre_Name):
        Data = pd.read_csv('lstm_price_prediction_potato.csv')
        # result = Data.loc[(Data['Centre_Name'] == Centre_Name & (Data['Date'] == Date), 'Predicted_Retail_Price'].values
        result = {
            'Predicted_Retail_Price': Data.loc[(Data['Date'] == Date) & (Data['Centre_Name'] == Centre_Name), 'Predicted_Retail_Price'].values[0]}
        return jsonify(result)

    def get_onion_prediction(self, Date, Centre_Name):
        Data = pd.read_csv('lstm_price_prediction_onion.csv')
        # result = Data.loc[(Data['Centre_Name'] == Centre_Name & (Data['Date'] == Date), 'Predicted_Retail_Price'].values
        result = {
            'Predicted_Retail_Price': Data.loc[(Data['Date'] == Date) & (Data['Centre_Name'] == Centre_Name), 'Predicted_Retail_Price'].values[0]}
        return jsonify(result)

    def get_cabbage_prediction(self, Date, Centre_Name):
        Data = pd.read_csv('lstm_price_prediction_cabbage.csv')
        # result = Data.loc[(Data['Centre_Name'] == Centre_Name & (Data['Date'] == Date), 'Predicted_Retail_Price'].values
        result = {
            'Predicted_Retail_Price': Data.loc[(Data['Date'] == Date) & (Data['Centre_Name'] == Centre_Name), 'Predicted_Retail_Price'].values[0]}
        return jsonify(result)

    def get_brinjal_prediction(self, Date, Centre_Name):
        Data = pd.read_csv('lstm_price_prediction_brinjal.csv')
        # result = Data.loc[(Data['Centre_Name'] == Centre_Name & (Data['Date'] == Date), 'Predicted_Retail_Price'].values
        result = {
            'Predicted_Retail_Price': Data.loc[(Data['Date'] == Date) & (Data['Centre_Name'] == Centre_Name), 'Predicted_Retail_Price'].values[0]}
        return jsonify(result)
