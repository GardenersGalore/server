from flask import Flask
from flask_restful import Api
from endpoints.PlantEndpoint import PlantEndpoint
from endpoints.PlantingEndpoint import PlantingEndpoint
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

# the main api that we can use:
# https://github.com/Growstuff/growstuff/wiki/API-Version-0

MONGO_URI=os.getenv("MONGO_URI")

connect(host=MONGO_URI)

app = Flask(__name__)
api = Api(app)


# add the different routes here
api.add_resource(PlantEndpoint, '/plant')
api.add_resource(PlantingEndpoint, '/planting')

if __name__ == '__main__':
    app.run(debug=True)