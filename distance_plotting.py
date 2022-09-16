import matplotlib.pyplot as plt
import pandas as pd

from diversity_calculations import *

DATA_LIMIT = 10  # limit the data for dev
data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)
features_strings = ['feature_ego_speed', 'feature_ego_acceleration']
feature_objects = feature_stats(data, features_strings)
normalise_feature_values(data, feature_objects)

manhattan_div = []
for i in range(len(data.index)):
    manhattan_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'manhattan'), 4))

euclidean_div = []
for i in range(len(data.index)):
    euclidean_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'euclidean'), 4))

print(manhattan_div, euclidean_div)


plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
