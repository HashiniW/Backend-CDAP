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

    def get_tomato_prediction(self, centre_name, date):
        data = pd.read_csv('lstm_price_prediction_tomato.csv')
        # result = data.loc[(data['centre_name'] == centre_name & (data['date'] == date), 'predicted_retail_price'].values
        result = {
            'predicted_retail_price': data.loc[(data['centre_name'] == centre_name) & (data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_potato_prediction(self, centre_name, date):
        data = pd.read_csv('lstm_price_prediction_potato.csv')
        # result = data.loc[(data['centre_name'] == centre_name & (data['date'] == date), 'predicted_retail_price'].values
        result = {
            'predicted_retail_price': data.loc[(data['centre_name'] == centre_name) & (data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_onion_prediction(self, centre_name, date):
        data = pd.read_csv('lstm_price_prediction_onion.csv')
        # result = data.loc[(data['centre_name'] == centre_name & (data['date'] == date), 'predicted_retail_price'].values
        result = {
            'predicted_retail_price': data.loc[(data['centre_name'] == centre_name) & (data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_cabbage_prediction(self, centre_name, date):
        data = pd.read_csv('lstm_price_prediction_cabbage.csv')
        # result = data.loc[(data['centre_name'] == centre_name & (data['date'] == date), 'predicted_retail_price'].values
        result = {
            'predicted_retail_price': data.loc[(data['centre_name'] == centre_name) & (data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)

    def get_brinjal_prediction(self, centre_name, date):
        data = pd.read_csv('lstm_price_prediction_brinjal.csv')
        # result = data.loc[(data['centre_name'] == centre_name & (data['date'] == date), 'predicted_retail_price'].values
        result = {
            'predicted_retail_price': data.loc[(data['centre_name'] == centre_name) & (data['date'] == date), 'predicted_retail_price'].values[0]}
        return jsonify(result)
