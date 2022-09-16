"""
STEPS FOR DIVERSITY CALCULATIONS:
- read normalised data from 'diversity_input.csv'
- output results to 'diversity_output.csv'
"""

import pandas as pd
import statistics as stats
import csv


def kth_property_diversity(feature_name, scenario1, scenario2, overall_data):
    """
    Computes the kth property diversity PDIVk between two scenarios
    :param feature_name: the string name of the feature
    :param scenario1: int representing scenario no.
    :param scenario2: int representing scenario no.
    :param overall_data: Pandas DataFrame of data
    :return:
    """
    return abs(overall_data[feature_name][scenario1] - overall_data[feature_name][scenario2])


def overall_scenario_diversity(scenario, overall_data):
    """
    Determines the sum of the two-scenario diversities between
    scenario and every other scenario, SDIV.
    :param scenario: scenario to compute diversity metric for
    :param overall_data: dataset
    :return: Diversity metric
    """

    all_scenario_property_divs = []
    feature_names = list(overall_data.columns)
    no_of_features = len(feature_names)

    # for each feature, determine the property diversity between the two scenarios
    for i in range(0, len(overall_data.index)):
        # determine the property diversity
        two_scenario_property_divs = []
        if i != scenario:
            for feature in feature_names:
                two_scenario_property_divs.append(kth_property_diversity(feature, scenario, i, overall_data))
            all_scenario_property_divs.append(two_scenario_property_divs)

    # sum the two scenario diversity
    two_scenario_diversities = []  # diversity metric between scenario, and all other tests

    # Computing SDIV for each other scenario
    for i in range(0, len(all_scenario_property_divs)):
        diversity_sum = 0
        for j in range(0, no_of_features):
            diversity_sum += all_scenario_property_divs[i][j]
        two_scenario_diversities.append(diversity_sum / no_of_features)

    return sum(two_scenario_diversities)


def compute_diversity(overall_data):
    """
    Computes the diversity of all of the scenarios
    :param overall_data: DataFrame representation of original data
    :return: list of [scenario_no, scenario_diversity] for each
             scenario
    """
    print('\nComputing the diversity for all of the data...')
    diversity_res = []
    for i in range(len(overall_data)):
        diversity_res.append([i, round(overall_scenario_diversity(i, overall_data), 4)])
    print('\nCalculations Complete!')
    return diversity_res


def write_results_to_csv(diversity_results):
    """
    Writes the diversity results to an output csv file
    :param diversity_results: list of [scenario_no,
           scenario_diversity] for each scenario
    :return: n/a
    """
    print('\nWriting results to output csv file...')
    # open csv file in write mode
    with open('diversity_output.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['scenario no.', 'scenario diversity'])
        # write rows to file
        writer.writerows(diversity_results)
        print('Writing to file Complete!')

