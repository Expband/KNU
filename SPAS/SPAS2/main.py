import pandas as pd
import numpy as np

DatSetIris = pd.read_csv('iris.csv')
TrainDataSet = DatSetIris.sample(frac=0.9,random_state =1)
TestDataSet = DatSetIris.drop(TrainDataSet.index)
TrainCol = TrainDataSet.drop('variety',axis=1).values
TrainRow = TrainDataSet['variety'].values
TestCol = TestDataSet.drop('variety',axis=1).values
TestRow = TestDataSet['variety'].values

def conusdistance(u,v):
    return 1 - np.dot(u,v)/(np.sqrt(np.sum(u**2))*np.sqrt(np.sum(v**2)))

neighbors = []

def findnearesneighbor(TrainCol,TrainRow,TestCol):
    for x in TestCol:
        distance = [conusdistance(x,y) for y in TrainCol]
        nearest_index = np.argmin(distance)
        neighbors.append(TrainRow[nearest_index])
    return  np.array(neighbors)
def results(TestRow,neighbors):
    accuracy = np.sum(TestRow == predictions) / len(TestRow)
    for i in range(len(neighbors)):
        print(f'Predicted: {neighbors[i]}, Actual: {[i]}')
    print(f'\nAccuracy: {accuracy}')
predictions = findnearesneighbor(TrainCol , TrainRow , TestCol)
results(TestRow, neighbors)
