from flask import request, session, jsonify , make_response
from src.repositories.repositori import Repositori


class Services:

    def __init__(self):
        self.repo = Repositori()

    def registrationService(self, data):
        self.makeSession(data)
        self.repo.insertData(data)
        return data

    def compareLoginData(self, data):
        login = data['login']
        self.compareSession(data)
        password = data['password']
        print(login , password)
        foundUser = self.repo.getUserByLogin(login)
        print(foundUser)
        return 1

    def makeSession(self, data):
        if request.method == 'POST':
            session['login'] = data['login']
            print(session)

    def compareSession(self, data):
        if str(data['login']) in session:
            existSession = bool(True)
            print(existSession)
            print(session)
        else: print('session isn`t exist')

    def find_max_local_minimum(arr):
        max_local_min = float('-inf')

        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                if arr[i] > max_local_min:
                    max_local_min = arr[i]

        return max_local_min
