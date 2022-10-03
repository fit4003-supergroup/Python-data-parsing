"""
STEPS FOR DIVERSITY CALCULATIONS:
- read normalised data from 'diversity_input.csv'
- output results to 'diversity_output.csv'
"""
import numpy as np
import pandas as pd
import statistics as stats
import csv
import math


def overall_scenario_diversity(scenario, overall_data, distance_type = 'manhattan'):
    """
    Determines the sum of the two-scenario diversities between
    scenario and every other scenario, SDIV.
    :param distance_type: distance algorithm, manhattan or euclidean
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
                print('scenario: ' + str(scenario) + ', i: '+str(i)+', feature: '+str(feature))
                difference = abs((overall_data[feature][scenario] - overall_data[feature][i]))
                if distance_type == 'manhattan':
                    two_scenario_property_divs.append(difference)
                elif distance_type == 'euclidean':
                    two_scenario_property_divs.append(difference**2)
                else:
                    raise Exception("distance_type must be one of 'manhattan','euclidean'")

            all_scenario_property_divs.append(two_scenario_property_divs)

    # sum the two scenario diversity
    two_scenario_diversities = []  # diversity metric between scenario, and all other tests

    # Computing SDIV for each other scenario
    for i in range(0, len(all_scenario_property_divs)):
        diversity_sum = np.nansum(all_scenario_property_divs[i])
        if distance_type == 'manhattan':
            two_scenario_diversities.append(diversity_sum / no_of_features)
        else:
            two_scenario_diversities.append(round(math.sqrt(diversity_sum) / no_of_features, 4))

    return sum(two_scenario_diversities)


def compute_diversity(overall_data):
    """
    Computes the diversity of all of the scenarios
    :param overall_data: DataFrame representation of original data
    :return: list of [scenario_no, scenario_diversity] for each
             scenario
    """
    print('Computing the diversity for all of the data...')
    diversity_res = []
    for i in range(len(overall_data)):
        diversity_res.append([i, round(overall_scenario_diversity(i, overall_data), 4)])
    print('Calculations Complete!')
    return diversity_res


def write_results_to_csv(diversity_results):
    """
    Writes the diversity results to an output csv file
    :param diversity_results: list of [scenario_no,
           scenario_diversity] for each scenario
    :return: n/a
    """
    print('Writing results to output csv file...')
    # open csv file in write mode
    with open('diversity_output.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['scenario no.', 'scenario diversity'])
        # write rows to file
        writer.writerows(diversity_results)
        print('Writing to file Complete!')


if __name__ == "__main__":
    # columns are diversity features and data is normalised
    processed_data = pd.read_csv('diversity_input.csv')

    # compute diversity
    diversities = compute_diversity(processed_data)

    # write to csv
    write_results_to_csv(diversities)
