from flask import request, make_response, jsonify
from flask_restful import Resource
from src.BusinessLogicLayer.IncedentService import IncedentService


class IncedentControler(Resource):

    def __init__(self):
        self.incedentService = IncedentService()

    def post(self):
        data = request.get_json()
        response = make_response(jsonify({'message': 'post_request_done'}), 200)
        self.incedentService.transferData(data)
        return response




