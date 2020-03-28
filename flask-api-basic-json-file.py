from flask import Flask, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


with open("flask-api-basic-json-file.json") as f:
    shops = json.load(f)

todos = {}


class Shops(Resource):
    def get(self):
        return jsonify({"Shops": shops})


api.add_resource(Shops, '/')

if __name__ == '__main__':
    app.run(port=8001, debug=True)