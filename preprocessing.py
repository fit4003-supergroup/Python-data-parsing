"""
file for pre-processing the data from the DataSetfeatues.csv file
the steps involved in this include:
- demand feature selection
    * conversion of categorical features to demand values
- diversity feature selection
    * outlier removal for diversity feature values
    * normalisation of diversity feature values

this file performs the pre-processing on the data and then
writes it to a new csv file for diversity and demand calcs
"""
import pandas as pd
import csv

"""
DEMAND PRE-PROCESSING
- define demand features
- convert any categorical features to corresponding demand values
- extract demand features and values from DataSetfeatures.csv
"""
feature_names = [
    'feature_ego_speedDemand',
    'feature_rainDemand',
    'feature_fogDemand',
    'feature_wetnessDemand',
    'feature_timeDemand',
    'feature_scenarioTrafficLightDemand',
    'feature_scenarioSideWalkDemand',
    'feature_totalNPCs',
    'feature_totalPedestrians',
    'feature_totalStaticObstacles',
    'feature_totalRoadUsers',
]

data = pd.read_csv('DataSetfeatures.csv')


class Feature:
    # object to store feature info
    def __init__(self, name, medium_demand, demand_values):
        self.name = name
        self.medium_demand = medium_demand
        self.demand_values = demand_values


def feature_stats(overall_data, feature_set):
    feature_objects = []
    for feature in feature_set:

        # get values
        demand_values = []
        for i in range(0, len(overall_data[feature])):
            demand_values += overall_data[feature][i]

        # get medium
        feature_min = min(overall_data[feature])
        feature_max = max(overall_data[feature])
        medium_demand = (feature_max - feature_min) / 2

        # create object to store
        feature_objects.append(Feature(feature, medium_demand, demand_values))

    return feature_objects


processed_demand_features = feature_stats(data, feature_names)
print(processed_demand_features[0].name)

with open('demand_input.csv', 'w') as file:
    # create csv writer
    writer = csv.writer(file)

    writer.writerow(feature_names)
    # writer.writerows(feature.demand_values)