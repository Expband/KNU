import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from collections import Counter
from sklearn import metrics
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

DataSet = pd.read_csv('dataset/seeds.csv')
DataSetSize = DataSet.iloc[:,:-1].values
DataSetClass = DataSet.iloc[:,7].values

ClusterFunction = KMeans(n_clusters=3)
ClusterFunction.fit(DataSetSize)
labels = ClusterFunction.labels_
metrics.silhouette_score(DataSetSize,labels,metric='minkowski')
Predictions = ClusterFunction.predict(DataSetSize)
DataSet['cluster']=Predictions

Centroid = ClusterFunction.cluster_centers_

count_clusters = Counter(labels)

fig , ax = plt.subplots()
ColorMap = ListedColormap(['crimson', 'mediumblue', 'darkmagenta','yellow','red','green','gold'])
ScatterMatrixResults = ax.scatter(DataSetSize[:,0],DataSetSize[:,5],c=Predictions,s=15,cmap =ColorMap)
ScatterMatrixCentroids = ax.scatter(Centroid[:,0],Centroid[:,5],marker='*',c='purple',s=200,label='centroids')
fig1 , ax1 = plt.subplots()
ScatterMatrixResults1 = ax1.scatter(DataSetSize[:,0],DataSetSize[:,4],c=Predictions,s=15,cmap =ColorMap)
ScatterMatrixCentroids1 = ax1.scatter(Centroid[:,0],Centroid[:,4],marker='*',c='purple',s=200,label='centroids')
fig2 , ax2 = plt.subplots()
ScatterMatrixResults2 = ax2.scatter(DataSetSize[:,0],DataSetSize[:,3],c=Predictions,s=15,cmap =ColorMap)
ScatterMatrixCentroids2 = ax2.scatter(Centroid[:,0],Centroid[:,3],marker='*',c='purple',s=200,label='centroids')
plt.show()


print(DataSet)
print(Centroid)
print(count_clusters)
