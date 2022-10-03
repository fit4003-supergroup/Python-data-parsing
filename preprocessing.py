from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile
import pandas as pd
import csv

"""
COMMON Diversity and Demand Pre-processing Steps:
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
    """
    Identifies key characteristics of the data for
    each feature in the feature set (min, max, medium)
    and creates a new Feature object with this data.
    :param overall_data: data read from og csv file
    :param feature_set: list of string names of features
    :return: list of Feature objects for each given
             feature in the feature set.
    """
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


"""
DEMAND PRE-PROCESSING
- define demand features
- convert any categorical features to corresponding demand values
- extract demand features and values from DataSetfeatures.csv

"""


def print_to_demand_csv(feature_names, processed_features):
    # write to output file
    with open('demand_input.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        # write column header names
        # write column names
        feature_names.insert(0, 'scenario_no')
        writer.writerow(feature_names)

        # create rows
        # for each row (i.e. data value)
        for i in range(0, len(processed_features[0].data_values)):
            # initialise row with 1st column as scenario id
            row_data = [i]
            # for each feature append feature data
            for j in range(0, len(processed_features)):
                row_data.append(processed_features[j].data_values[i])
            # write the row of data:
            writer.writerow(row_data)


"""
DIVERSITY PRE-PROCESSING
- define pre-processing features
- remove outliers of data
- normalisation of values
- write output to csv file
"""


def feature_outlier_identification(feature_object):
    """
    Identifies all scenarios which have a feature value
    that is an outlier
    :param feature_object: Feature instance
    :return: list of ints representing scenarios with
             outliers
    """
    iqr_values = feature_object.data_values
    # define inter-quartile range
    q25, q75 = percentile(iqr_values, 25), percentile(iqr_values, 75)
    iqr = q75 - q25
    # determine outlier cutoff
    iqr_cutoff = iqr * 1.5
    iqr_lower, iqr_upper = q25 - iqr_cutoff, q75 + iqr_cutoff

    # identify outliers
    iqr_outlier_scenarios = []
    for i in range(0, len(iqr_values)):
        if iqr_values[i] < iqr_lower or iqr_values[i] > iqr_upper:
            # print('feature ' + str(feature_object.name) + ' has outlier in scenario: ' + str(i))
            iqr_outlier_scenarios.append(i)
    return iqr_outlier_scenarios


def remove_outliers(diversity_features):
    """
    Removes outliers from the data
    :param diversity_features:
    :return:
    """
    print("Identifying Outliers...")
    # for each feature identify any scenarios with outliers
    outlier_scenarios = []
    for feature in diversity_features:
        outlier_scenarios += feature_outlier_identification(feature)

    # remove duplicates so scenarios aren't removed twice
    outlier_scenarios = list(dict.fromkeys(outlier_scenarios))

    print("Removing Outliers...")
    # remove the scenario data for outlier scenarios
    # for scenario in outlier_scenarios:
    #     for feature in diversity_features:
    #         feature.data_values.pop(scenario)
    print('Outlier removal Complete!')


def normalise_feature_values(feature_objects):
    """
    Normalises the feature values so they are
    all between 0-1
    :param feature_objects: Feature instances
    :return: n/a
    """
    print("Normalising Feature values...")
    for feature in feature_objects:
        diff = feature.max_value - feature.min_value
        for i in range(0, len(feature.data_values)):
            if diff == 0:
                normalised_value = 0
            else:
                normalised_value = (feature.data_values[i] - feature.min_value) / diff
            feature.data_values[i] = normalised_value
    print("Feature Normalisation Complete!")


def print_to_csv(feature_names, processed_features):
    """
    Output the processed data to a readable csv format
    :param feature_names: strings of feature names
    :param processed_features: processed data to be printed
    :return: n/a
    """
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
            # for each feature append feature data
            for j in range(0, len(processed_features)):
                row_data.append(processed_features[j].data_values[i])
            # write the row of data:
            writer.writerow(row_data)
