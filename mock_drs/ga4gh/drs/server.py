import string

from flask import current_app

from database.register_mongodb import create_mongo_client


def GetServiceInfo():
    return (
        {
            "version": "string",
            "title": "string",
            "description": "string",
            "contact": {},
            "license": {},
        },
        200,
    )


def GetBundle(bundle_id):
    return None


def GetObject(object_id: string):
    # create a client for the database
    mongo = create_mongo_client(app=current_app, config=current_app.config)

    # retrieve the object by id or throw a 404
    obj = mongo.db.data_objects.find_one_or_404({"id": object_id})
    obj.pop("_id")
    return obj, 200


def GetAccessURL(object_id, access_id):

    # create a client for the database
    mongo = create_mongo_client(app=current_app, config=current_app.config)

    # retrieve the object or throw a 404
    obj = mongo.db.data_objects.find_one_or_404({"id": object_id})

    # create the response
    response = obj["access_methods"][0]["access_url"]
    return response, 200
