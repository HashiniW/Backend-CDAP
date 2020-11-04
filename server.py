from flask import Flask
from routes.suplier_route import suplier_blueprint
from flask_cors import CORS

server = Flask(__name__)
CORS(server)
server.config.from_object('config')

server.register_blueprint(suplier_blueprint)

if __name__ == '__main__':   
    server.run()