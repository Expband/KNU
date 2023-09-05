import pandas as pd


class AvailablePlaces:
    @staticmethod
    def getByTheCity():
        df = pd.read_csv('flight_table.csv')
        print('Choose the city : ')
        destination = df['destination'].values
        print(destination)
        chosenCity = input()
        while chosenCity not in destination:
            chosenCity = input('Undefined city !')
        else:
            departureTime = df[df['destination'] == chosenCity]['avalieable_places'].values
            flightNumber = df[df['destination'] == chosenCity]['flight_number'].values
            print(f'Available places for flight number {flightNumber} : {departureTime}')
