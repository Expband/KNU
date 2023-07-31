import json
from bson import json_util
from pymongo.mongo_client import MongoClient
from flask import jsonify
from src.DataAccessLayer.ConfigParser import ConfigParser


class IncedentReposytori:

    def __init__(self):
        self.cfg = ConfigParser()
        self.uri = self.cfg.get_uri()
        self.client = MongoClient(self.uri)
        self.db = self.client[self.cfg.get_db()]
        self.collection = self.db[self.cfg.get_collection()]

    def addIncedent(self ,data):
        try:
            insert = self.collection.insert_one(data)
        except Exception as ex:
            print(ex)

    def getIncedents(self):
        try:
            foundData = self.collection.find()
            list_data = list(foundData)
            print(list_data)
            print(len(list_data))
            for i in range(len(list_data)):
                list_data[i] = json.loads(json_util.dumps(list_data[i]))
            return_data = {"data":list_data}
            return jsonify(return_data)
        except Exception as ex:
            print(ex)
