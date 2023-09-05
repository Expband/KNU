import pandas as pd


class DepartureTime:
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
            departureTime = df[df['destination'] == chosenCity]['departure_time'].values
            print(f'Departure time to {chosenCity} : {departureTime}')
