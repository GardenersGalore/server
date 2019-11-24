"""
This model is for the garden

"""

from mongoengine import Document, IntField, StringField


class Plant(Document):
    name = StringField(unique=True, required=True)
    en_wikipedia_url = StringField()
    binomial_name = StringField()  # binomial_name
    description = StringField()
    median_lifespan = IntField()
    median_days_to_first_harvest = IntField()
    median_days_to_last_harvest = IntField()
    height = IntField()
    spread = IntField()
    row_spacing = IntField()
    sowing_method = StringField()
    sun_requirements = StringField()
    svg_icon = StringField()
    pictureURL = StringField()
