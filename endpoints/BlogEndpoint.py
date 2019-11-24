import json

from flask import request
from flask_restful import Resource, abort

from models.Blog import Blog

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class BlogEndpoint(Resource):
    def post(self):
        j = request.get_json()

        # need to ensure the required fields are in the json
        print("IN HERE")

        if "name" not in j:
            abort(422, message="name is not in json body")
        else:
            name = j["name"]

        if "username" not in j:
            abort(422, message="username not in json body")
        else:
            username = j["username"]

        if "content" not in j:
            abort(422, message="content not in json body")
        else:
            content = j["content"]

        blog_obj = Blog(
            name=name,
            username=username,
            content=content
        )

        print(blog_obj)

        if "tags" in j:
            blog_obj.tags = j["tags"]

        d = blog_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def get(self):
        pass
