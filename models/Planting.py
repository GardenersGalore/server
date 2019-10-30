"""
This model is for an instance of a plant that is within someones backyard

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, GeoPointField


class Planting(Document):
    plant_name = StringField()
    garden_name = StringField()
    coordinates = GeoPointField(unique_with=["plant_name", "garden_name"])
    planted_at = DateField()
    description = StringField()
    planted_from = StringField() # something like seed, sappling, established ect.
    harvest_count = IntField()
