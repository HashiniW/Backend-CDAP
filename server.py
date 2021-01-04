from flask import Flask, jsonify
from routes.lstm_price_route import lstm_blueprint
from flask_cors import CORS
import csv
import json


server = Flask(__name__)
CORS(server)
server.config.from_object('config')

server.register_blueprint(lstm_blueprint)

#Set csv file path that program should have to read
tomato_csvFilePath  = 'tomato.csv'
potato_csvFilePath  = 'potato.csv'
onion_csvFilePath   = 'onion.csv'
cabbage_csvFilePath = 'cabbage.csv'
brinjal_csvFilePath = 'brinjal.csv'

#Set path and file name for json file that system should be created
tomato_jsonFilePath  = 'tomato.json'
potato_jsonFilePath  = 'potato.json'
onion_jsonFilePath   = 'onion.json'
cabbage_jsonFilePath = 'cabbage.json'
brinjal_jsonFilePath = 'brinjal.json'

#Create service for read curret updated csv and create json file
@server.route('/tomatocsv')
def tomato_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(tomato_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(tomato_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/potatocsv')
def potato_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(potato_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(potato_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/onioncsv')
def onion_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(onion_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(onion_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/cabbagecsv')
def cabbage_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(cabbage_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(cabbage_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')

#Create service for read curret updated csv and create json file
@server.route('/brinjalcsv')
def brinjal_csv_json():
    #create object to store rows in csv file
    data={}
    #initialize the object index
    i = 0
    #start reading csv file
    with open(brinjal_csvFilePath) as f:
        #Create file reader
        csvReader = csv.DictReader(f)
        #loop through the rows that read by file reader
        for rows in csvReader:
            id = i #set object id 0 to number of rows - 1 in csv file
            data[id] = rows #set current row as object
            i = i+1 #increase id by 1

    #open file reder for create JSON file with CSV data
    with open(brinjal_jsonFilePath, "w") as jf:
        #Write CSV data to JSON
        jf.write(json.dumps(data, indent=4))

    return json.dumps('Done')


#Return Tomato Data
@server.route('/tomato/<date>/<centre_name>')
def create_json_obj_tomato():
   resp =  create_json_tomato()
   return json.dumps(resp)

#Filter out data from JSON and select data for tomato
def create_json_tomato():
    # Create empty list
    final_json = []

    #Read tomato.json file and assign values to variable
    with open('./tomato.json') as f:
        tomato = json.load(f)

    #modify and create JSON object for each record
    for i in range(len(tomato)):
        #read each object in JSON file
        json_obj = tomato[str(i)]
        #Filter data for tomato and select records for centre Pettah, Dambulla, Jaffna
        if json_obj["commodity_name"] == "tomato" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'tomato'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "Pettah"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "Dambulla"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "Jaffna"

            #Append modified record to final object
            final_json.append(json_obj)

    return final_json

#Return Potato Data
@server.route('/potato/<date>/<centre_name>')
def create_json_obj_potato():
   resp =  create_json_potato()
   return json.dumps(resp)

#Filter out data from JSON and select data for potato
def create_json_potato():
    # Create empty list
    final_json = []

    #Read potato.json file and assign values to variable
    with open('./potato.json') as f:
        potato = json.load(f)

    #create JSON object for each record
    for i in range(len(potato)):
        json_obj = potato[str(i)]
        if json_obj["commodity_name"] == "potato" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'potato'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "Pettah"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "Dambulla"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "Jaffna"

            final_json.append(json_obj)

    return final_json

#Return Onion Data
@server.route('/onion/<date>/<centre_name>')
def create_json_obj_onion():
   resp =  create_json_onion()
   return json.dumps(resp)

#Filter out data from JSON and select data for onion
def create_json_store3():
    # Create empty list
    final_json = []

    #Read onion.json file and assign values to variable
    with open('./onion.json') as f:
        onion = json.load(f)

    #create JSON object for each record
    for i in range(len(onion)):
        json_obj = onion[str(i)]
        if json_obj["commodity_name"] == "onion" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'onion'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "Pettah"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "Dambulla"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "Jaffna"

            final_json.append(json_obj)

    return final_json

#Return Cabbage Data
@server.route('/cabbage/<date>/<centre_name>')
def create_json_obj_cabbage():
   resp =  create_json_cabbage()
   return json.dumps(resp)

#Filter out data from JSON and select data for cabbage
def create_json_cabbage():
    # Create empty list
    final_json = []

    #Read cabbage.json file and assign values to variable
    with open('./cabbage.json') as f:
        cabbage = json.load(f)

    #create JSON object for each record
    for i in range(len(cabbage)):
        json_obj = cabbage[str(i)]
        if json_obj["commodity_name"] == "cabbage" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'cabbage'

            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "Pettah"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "Dambulla"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "Jaffna"

            final_json.append(json_obj)

    return final_json

#Return Brinjal Data
@server.route('/brinjal/<date>/<centre_name>')
def create_json_obj_brinjal():
   resp =  create_json_brinjal()
   return json.dumps(resp)

#Filter out data from JSON and select data for brinjal
def create_json_brinjal():
    # Create empty list
    final_json = []

    #Read brinjal.json file and assign values to variable
    with open('./brinjal.json') as f:
        brinjal = json.load(f)

    #create JSON object for each record
    for i in range(len(brinjal)):
        json_obj = brinjal[str(i)]
        if json_obj["commodity_name"] == "brinjal" and (json_obj["centre_name"] == "DELHI" or json_obj["centre_name"] == "KOLKATA" or json_obj["centre_name"] == "MUMBAI"):
            json_obj["commodity_name"] = 'brinjal'
            
            #Modify centre names
            if json_obj["centre_name"] == "DELHI":
                json_obj["centre_name"] = "Pettah"
            elif json_obj["centre_name"] == "KOLKATA":
                json_obj["centre_namem"] = "Dambulla"
            elif json_obj["centre_name"] == "MUMBAI":
                json_obj["centre_name"] = "Jaffna"

            final_json.append(json_obj)

    return final_json


if __name__ == '__main__':
    server.run()
