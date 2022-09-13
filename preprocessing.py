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
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile
import pandas as pd
import csv

"""
COMMON DATA:
- Feature class used to store info about the features in use
- feature statistics needed for the calculations
- reading the csv file for use
"""


class Feature:
    # object to store feature info
    def __init__(self, name, min_value, max_value, medium_demand, data_values):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.medium_demand = medium_demand
        self.data_values = data_values


def feature_stats(overall_data, feature_set):
    feature_objects = []
    for feature in feature_set:
        # get values
        data_values = []
        for i in range(0, len(overall_data[feature])):
            data_values.append(overall_data[feature][i])

        # get medium
        feature_min = min(overall_data[feature])
        feature_max = max(overall_data[feature])
        medium_demand = (feature_max - feature_min) / 2

        # create object to store
        feature_objects.append(Feature(feature, feature_min, feature_max, medium_demand, data_values))

    return feature_objects


# read the csv file
DATA_LIMIT = 100
data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)

"""
DEMAND PRE-PROCESSING
- define demand features
- convert any categorical features to corresponding demand values
- extract demand features and values from DataSetfeatures.csv

TODO:
- write data rows in
"""
demand_feature_names = [
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

processed_demand_features = feature_stats(data, demand_feature_names)


def print_to_demand_csv(feature_names, processed_features):
    # write to output file
    with open('demand_input.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        # write column header names
        column_headers = ['scenario no.', feature_names]
        writer.writerow(column_headers)


print_to_demand_csv(demand_feature_names, processed_demand_features)

"""
DIVERSITY PRE-PROCESSING
- define pre-processing features
- remove outliers of data
- normalisation of values
- write output to csv file
"""

diversity_feature_names = [
    'feature_ego_acceleration',
    'feature_ego_speed',
    'feature_totalNPCs',
    'feature_totalPedestrians',
    'feature_totalStaticObstacles',
    'feature_totalRoadUsers',
    'feature_obstaclesAverageDistance',
]

# get feature stats
processed_diversity_features = feature_stats(data, diversity_feature_names)

"""
outlier removal:
- find outlier in feature data
- identify which scenario this belongs to 
- remove the all of the feature values for this scenario

TODO:
- fix removal of outliers so that if there are two features
  that are outliers for the same scenario the removal is not
  duplicated (i.e. accidental removal of good data)
"""


def feature_outlier_identification(feature_object):
    # get values
    # print('feature_object.data_values: ' + str(feature_object.data_values))
    iqr_values = feature_object.data_values

    # define inter-quartile range
    q25, q75 = percentile(iqr_values, 25), percentile(iqr_values, 75)
    iqr = q75 - q25

    # determine outlier cutoff
    iqr_cutoff = iqr * 1.5
    iqr_lower, iqr_upper = q25 - iqr_cutoff, q75 + iqr_cutoff

    # identify outliers
    iqr_outliers = [y for y in iqr_values if y < iqr_lower or y > iqr_upper]
    iqr_outlier_scenarios = []
    for i in range(0, len(iqr_values)):
        if iqr_values[i] < iqr_lower or iqr_values[i] > iqr_upper:
            print('feature ' + str(feature_object.name) + ' has outlier in scenario: ' + str(i))
            iqr_outlier_scenarios.append(i)
    print('outlier scenarios: ' + str(iqr_outlier_scenarios))
    return iqr_outlier_scenarios


def remove_outliers(diversity_features):
    print("\n*********************************")
    print("REMOVING OUTLIERS    ...")
    print("*********************************")

    # for each feature identify any scenarios with outliers
    outlier_scenarios = []
    for feature in diversity_features:
        outlier_scenarios += feature_outlier_identification(feature)
    print('overall outlier scenarios: ' + str(outlier_scenarios))

    # remove the scenario data for outlier scenarios
    for scenario in outlier_scenarios:
        print('removing data for scenario ' + str(scenario))
        for feature in diversity_features:
            feature.data_values.pop(scenario)


remove_outliers(processed_diversity_features)


# normalise data values
def normalise_feature_values(feature_objects):
    print("\n*********************************")
    print("NORMALISING FEATURE VALUES    ...")
    print("*********************************")
    for feature in feature_objects:
        print('\nfeature name: ' + str(feature.name))
        diff = feature.max_value - feature.min_value
        for i in range(0, len(feature.data_values)):
            normalised_value = (feature.data_values[i] - feature.min_value) / diff
            # print('normalised value: ' + str(normalised_value))
            feature.data_values[i] = normalised_value


normalise_feature_values(processed_diversity_features)


def print_to_csv(feature_names, processed_features):
    # write to document
    with open('diversity_input.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        # write column names
        feature_names.insert(0, 'scenario_no')
        writer.writerow(feature_names)

        # create rows
        # for each row (i.e. each data value)
        for i in range(0, len(processed_features[0].data_values)):
            # initialise row with 1st column as scenario id
            row_data = [i]
            print('compiling data for row ' + str(i) + ' ...')
            # for each feature append feature data
            for j in range(0, len(processed_features)):
                row_data.append(processed_features[j].data_values[i])
            print('row ' + str(i) + ' data: ' + str(row_data))
            # write the row of data:
            writer.writerow(row_data)


print_to_csv(diversity_feature_names, processed_diversity_features)
