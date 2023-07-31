from flask import request, make_response, jsonify
from flask_restful import Resource
from src.services.services import Services


class RegistrationControler(Resource):

    def __init__(self):
        self.services = Services()

    def post(self):
        data = request.get_json()
        response = make_response(jsonify({'message': 'post_request_done'}), 200)
        self.services.registrationService(data)
        print(data)
        return response


class LoginControler(Resource):

    def __init__(self):
        self.services = Services()

    def post(self):
        data = request.get_json()
        response = make_response(jsonify({'message': 'post_request_done'}), 200)
        self.services.compareLoginData(data)
        return response
