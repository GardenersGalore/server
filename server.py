import os
import ssl

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from mongoengine import connect

from endpoints.AnswerEndpoint import AnswerEndpoint
from endpoints.BlogEndpoint import BlogEndpoint
from endpoints.GardenEndpoint import GardenEndpoint
from endpoints.GardenSearchEndpoint import GardenSearchEndpoint
from endpoints.GardensEndpoint import GardensEndpoint
from endpoints.PlantEndpoint import PlantEndpoint
from endpoints.PlantGardenSearchEndpoint import PlantGardenSearchEndpoint
from endpoints.PlantInfoEndpoint import PlantInfoEndpoint
from endpoints.PlantSearchEndpoint import PlantSearchEndpoint
from endpoints.PlantingEndpoint import PlantingEndpoint
from endpoints.PlantingsEndpoint import PlantingsEndpoint
from endpoints.QuestionEndpoint import QuestionEndpoint
from endpoints.QuestionSearchEndpoint import QuestionSearchEndpoint
from endpoints.QuestionsEndpoint import QuestionsEndpoint
from endpoints.UserAllEndpoint import UserAllEndpoint
from endpoints.UserEndpoint import UserEndpoint
from endpoints.UserSearchEndpoint import UserSearchEndpoint
from endpoints.WeatherEndpoint import WeatherEndpoint

load_dotenv()

# the main api that we can use:
# https://github.com/Growstuff/growstuff/wiki/API-Version-0

MONGO_URI = os.getenv("MONGO_URI")

connect(host=MONGO_URI, ssl_cert_reqs=ssl.CERT_NONE)

app = Flask(__name__)
CORS(app)
api = Api(app)

# add the different routes here
api.add_resource(UserEndpoint, '/user')
api.add_resource(UserAllEndpoint, '/userall')
api.add_resource(PlantEndpoint, '/plant')
api.add_resource(PlantInfoEndpoint, '/plantinfo')
api.add_resource(PlantingEndpoint, '/planting')
api.add_resource(WeatherEndpoint, '/weather')
api.add_resource(PlantingsEndpoint, '/plantings')
api.add_resource(GardenEndpoint, '/garden')
api.add_resource(GardensEndpoint, '/gardens')
api.add_resource(QuestionEndpoint, '/forum/question')
api.add_resource(AnswerEndpoint, '/forum/answer')
api.add_resource(PlantGardenSearchEndpoint, '/gardenPlant-search')
api.add_resource(PlantSearchEndpoint, '/plant-search')
api.add_resource(GardenSearchEndpoint, '/garden-search')
api.add_resource(UserSearchEndpoint, '/user-search')
api.add_resource(QuestionsEndpoint, '/forum/questions')
api.add_resource(QuestionSearchEndpoint, '/question-search')
api.add_resource(BlogEndpoint, '/blog')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
