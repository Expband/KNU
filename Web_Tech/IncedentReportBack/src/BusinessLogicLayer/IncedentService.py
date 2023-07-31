from src.DataAccessLayer.IncedentRepository import IncedentReposytori
from flask import jsonify


class IncedentService():

    def __init__(self):
        self.incedentRepository = IncedentReposytori()

    def transferData(self, data):
        self.incedentRepository.addIncedent(data)
        return data

    def transferIncedentUp(self):
        incedent = self.incedentRepository.getIncedents()
        return incedent




