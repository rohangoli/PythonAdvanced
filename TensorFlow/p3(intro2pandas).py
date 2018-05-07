import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

print city_names
print population

sampleDF = pd.DataFrame({ 'City name': city_names, 'Population': population })

print sampleDF


california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

print california_housing_dataframe.describe()

print "Cal House DF HEAD\n",california_housing_dataframe.head()

## print california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print type(cities['City name'])
print cities['City name']

print type(cities['City name'][1])
print cities['City name'][1]

print type(cities[0:2])
print cities[0:2]

print population/1000

import numpy as np
print np.log(population)
