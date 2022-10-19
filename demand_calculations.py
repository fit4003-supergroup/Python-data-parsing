"""
STEPS FOR DEMAND CALCULATIONS:
- read normalised data from 'demand_input.csv'
- output results to 'demand_output.csv'
"""
import pandas as pd
import csv


class Feature:
    """
    Object to store feature info
    """
    def __init__(self, name, medium_demand):
        self.name = name
        self.medium_demand = medium_demand


def feature_stats(overall_data, feature_set):
    """
    Determines the min, max and medium for
    each of the features and creates a Feature
    object to return.
    :param overall_data:
    :param feature_set:
    :return:
    """
    feature_objects = []
    for feature in feature_set:
        feature_min = min(overall_data[feature])
        feature_max = max(overall_data[feature])
        medium_demand = (feature_max - feature_min) / 2
        feature_objects.append(Feature(feature, medium_demand))

    return feature_objects


def feature_demand(scenario, feature):
    """
    Determines whether a feature is high demand
    compare to data medium
    :param scenario:
    :param feature:
    :return: 1 if high demand feature value
             0 if not high demand feature value
    """
    # compare to scenario demand value
    feature_value = scenario[feature.name]

    # if > medium then high demand
    if feature_value > feature.medium_demand:
        return 1
    else:  # if < medium then low demand
        return 0


def individual_scenario_demand(scenario_num, overall_data, feature_objects):
    """
    Calculates the total demand for the given scenario
    The most demanding scenarios will have highest total
    :param scenario_num: int representing scenario for calcs
    :param overall_data: DataFrame of processed data
    :param feature_objects: Feature instances
    :return:
    """
    scenario = overall_data.iloc[scenario_num]

    # for each feature in the feature set,
    # add demand to sum
    demand_sum = 0
    for feature in feature_objects:
        demand_sum += feature_demand(scenario, feature)

    return demand_sum


def scenario_demands(overall_data, feature_objects):
    """
    Calculates the demand values for all scenarios
    :param feature_objects:
    :param overall_data: DataFrame of processed data
    :return: list of demand values
    """
    print('Calculating Scenario Demands...')
    demands = []
    for i in range(0, len(overall_data)):
        demands.append(individual_scenario_demand(i, overall_data, feature_objects))
    print('Calculations Complete!')
    return demands


def write_output_to_csv(demand_results):
    """
    Writes demand calculation results to
    output file.
    :param demand_results: list of demand values
    :return: n/a
    """
    print('Writing results to output csv file...')
    # open csv file in write mode
    with open('demand_output.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['scenario no.', 'scenario demand'])
        # write rows to file
        for i in range(0, len(demand_results)):
            writer.writerow([i+1, demand_results[i]])
    print('Writing to file Complete!')

