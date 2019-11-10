from flask import Flask
from flask_restful import Api
from endpoints.PlantEndpoint import PlantEndpoint
from endpoints.PlantingEndpoint import PlantingEndpoint
from endpoints.WeatherEndpoint import WeatherEndpoint
from endpoints.PlantingsEndpoint import PlantingsEndpoint
from endpoints.GardenEndpoint import GardenEndpoint
from endpoints.GardensEndpoint import GardensEndpoint
from endpoints.PlantGardenEndpoint import PlantGardenEndpoint
from endpoints.QuestionEndpoint import QuestionEndpoint
from endpoints.AnswerEndpoint import AnswerEndpoint
from endpoints.QuestionsEndpoint import QuestionsEndpoint
from mongoengine import connect
from dotenv import load_dotenv
import os
from flask_cors import CORS
import ssl

load_dotenv()

# the main api that we can use:
# https://github.com/Growstuff/growstuff/wiki/API-Version-0

MONGO_URI=os.getenv("MONGO_URI")

connect(host=MONGO_URI, ssl_cert_reqs=ssl.CERT_NONE)

app = Flask(__name__)
CORS(app)
api = Api(app)


# add the different routes here
api.add_resource(PlantEndpoint, '/plant')
api.add_resource(PlantingEndpoint, '/planting')
api.add_resource(WeatherEndpoint, '/weather')
api.add_resource(PlantingsEndpoint, '/plantings')
api.add_resource(GardenEndpoint, '/garden')
api.add_resource(GardensEndpoint, '/gardens')
api.add_resource(PlantGardenEndpoint, '/plant-garden')
api.add_resource(QuestionsEndpoint, '/forum/questions')
api.add_resource(QuestionEndpoint, '/forum/question')

if __name__ == '__main__':
    app.run(debug=True, port=3000)