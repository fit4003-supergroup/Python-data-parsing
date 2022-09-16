# code to parse and analyse features from DataSetfeatures file
# *note: assumes file 'DataSetFeatures.csv' is in same folder
import pandas as pd
import statistics as stats
import csv
import math


class Feature:
    # object to store feature info
    def __init__(self, name, minimum, maximum):
        self.name = name
        self.minimum = minimum
        self.maximum = maximum


def feature_stats(overall_data, feature_set):
    # determine the feature statistics for each feature
    # min and max for normalising
    print("*********************************")
    print("CALCULATING FEATURE STATISTICS...")
    print("*********************************")
    feature_objects = []
    for feature in feature_set:
        feature_min = min(overall_data[feature])
        feature_max = max(overall_data[feature])
        feature_objects.append(Feature(feature, feature_min, feature_max))

    for feature in feature_objects:
        print('\nfeature name: ' + str(feature.name))
        print('feature minimum: ' + str(feature.minimum))
        print('feature maximum: ' + str(feature.maximum))

    return feature_objects


def normalise_feature_values(overall_data, feature_objects):
    print("\n*********************************")
    print("NORMALISING FEATURE VALUES    ...")
    print("*********************************")
    for feature in feature_objects:
        print('\nfeature name: ' + str(feature.name))
        diff = feature.maximum - feature.minimum
        for i in range(0, len(overall_data[feature.name])):
            normalised_value = (overall_data[feature.name][i] - feature.minimum) / diff
            overall_data[feature.name][i] = normalised_value
            # print('normalised value: ' + str(normalised_value))

def overall_scenario_diversity(scenario, overall_data, feature_objects, distance_type = 'manhattan'):
    """
    Determines the sum of the two-scenario diversities between
    scenario and every other scenario, SDIV.
    :param scenario: scenario to compute diversity metric for
    :param overall_data: dataset
    :param feature_objects: list of features to
    :return: Diversity metric
    """

    # for each feature, determine the property diversity between the two scenarios
    all_scenario_property_divs = []
    for i in range(0, len(overall_data.index)):
        # determine the property diversity
        two_scenario_property_divs = []
        if i != scenario:
            for feature in feature_objects:
                difference = abs((overall_data[feature.name][scenario] - overall_data[feature.name][i]))
                if distance_type == 'manhattan':
                    two_scenario_property_divs.append(difference)
                elif distance_type == 'euclidean':
                    two_scenario_property_divs.append(difference**2)
                else:
                    raise Exception("distance_type must be one of 'manhattan','euclidean'")
                # print('two_scenario_property_divs: ' + str(two_scenario_property_divs))
            all_scenario_property_divs.append(two_scenario_property_divs)
    # print('all_scenario_property_divs: '+str(all_scenario_property_divs))

    # sum the two scenario diversity
    two_scenario_diversities = [] # diversity metric between scenario, and all other tests

    # Computing SDIV for each other scenario
    for i in range(0, len(all_scenario_property_divs)):
        diversity_sum = sum(all_scenario_property_divs[i])
        if distance_type == 'manhattan':
            two_scenario_diversities.append(diversity_sum / len(feature_objects))
        else:
            two_scenario_diversities.append(round(math.sqrt(diversity_sum) / len(feature_objects),4))

    # print("Scenario " + str(scenario + 1) + " diversity: " + str(round(sum(two_scenario_diversities), 4)) + ", average: " +
    #       str(round(stats.mean(two_scenario_diversities), 4)))
    return sum(two_scenario_diversities)


def suite_diversity(data, feature_objects):
    """
    Runs scenario diversity for each scenario. I don't think the total suite diversity metric
    is very useful as it would increase at an exponential rate based on the number of scenarios
    :param data:
    :param feature_objects:
    :return:
    """
    print("\n*********************************")
    print("CALCULATING DIVERSITY METRICS ...")
    print("*********************************")

    diversity_sum = 0
    for i in range(len(data.index)):
        diversity_sum += overall_scenario_diversity(i, data, feature_objects)
    return diversity_sum

def write_to_csv(diversity_results):
    # open csv file in write mode
    with open('diversity_output.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['scenario no.', 'scenario diversity'])
        # write rows to file
        writer.writerows(diversity_results)

if __name__ == "__main__":
    # STEPS FOR DIVERSITY CALCS
    # 1. extract data from csv
    # we want to map the information in each row to a dictionary
    # whose keys are are given by a fieldnames parameter
    DATA_LIMIT = 1000  # limit the data for dev
    data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)

    # 2. find feature statistics (min, max, etc.)
    # included diversity features:
    features_strings = ['feature_ego_speed', 'feature_totalNPCs']
    feature_objects = feature_stats(data, features_strings)

    # 3. normalise the property data so that the values fall between 0 and 1
    normalise_feature_values(data, feature_objects)

    # 4. Compute test suite diversity across all scenarios
    # print("Total suite diversity: " + str(suite_diversity(data, feature_objects)))
    diversity_res = []
    for i in range(len(data.index)):
        diversity_res.append([i, round(overall_scenario_diversity(i, data, feature_objects), 4)])

    # 5. write output to csv file
    write_to_csv(diversity_res)
