from flask import jsonify
import json
from bson import json_util
from pymongo.mongo_client import MongoClient
from src.repositories.ConfigParser import ConfigParser


class Repositori():

    def __init__(self):
        self.cfg = ConfigParser()
        self.uri = self.cfg.get_uri()
        self.client = MongoClient(self.uri)
        self.db = self.client[self.cfg.get_db()]
        self.collection = self.db[self.cfg.get_collection()]

    def insertData(self, data):
        try:
            insert = self.collection.insert_one(data)
        except Exception as ex:
            print(ex)

    def getUserByLogin(self, login):
        try:
            foundData = self.collection.find_one({'login': str(login)})
            print(foundData)
            return foundData
        except Exception as ex:
            print(ex)
