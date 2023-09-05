from AvailablePlaces import AvailablePlaces
from DepartureTime import DepartureTime

print('Choose the action please . Available actions : ')
print('1)Departure time(you should choose the city)')
print('2)Available places(you should choose the city)')
chosenAction = input('Action : ')
departmentTime = DepartureTime()
availablePlaces = AvailablePlaces()
if chosenAction == '1':
    departmentTime.getByTheCity()
elif chosenAction == '2':
    availablePlaces.getByTheCity()
else:
    while chosenAction != '1' or chosenAction != '2':
        print('Wrong action')
        chosenAction = input('Action : ')
