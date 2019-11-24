"""
This model is for an instance of a plant that is within someones backyard

"""
import datetime

from mongoengine import Document, IntField, StringField, DateTimeField


class Planting(Document):
    plant_name = StringField(required=True)
    garden_name = StringField(required=True)
    x_coord = IntField(required=True)
    y_coord = IntField(required=True, unique_with=["garden_name", "x_coord"])
    planted_at = DateTimeField(default=datetime.datetime.utcnow)
    description = StringField()
    planted_from = StringField()  # something like seed, sappling, established ect.
    harvest_count = IntField()
    pictureURL = StringField()
