from flask_restful import Resource
from flask import jsonify, make_response
from src.BusinessLogicLayer.IncedentService import IncedentService


class IncedentControlerGet(Resource):

    def get(self):
        IS = IncedentService()
        res = IS.transferIncedentUp()
        return make_response(jsonify(res.json),200)


