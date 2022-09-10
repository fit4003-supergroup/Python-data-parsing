# code to parse and analyse features from DataSetfeatures file
# *note: assumes file 'DataSetFeatures.csv' is in same folder
import pandas as pd
import statistics as stats


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
            # print('normalised value: ' + str(normalised_value))
            overall_data[feature.name][i] = normalised_value


def kth_property_diversity(feature_name, scenario1, scenario2, overall_data):
    # computes the kth property diversity PDIVk between two scenarios
    # scenario1 and 2 are int values representing scenario name
    return abs(overall_data[feature_name][scenario1] - overall_data[feature_name][scenario2])


def two_scenario_diversity(prop_diversities):
    # computes the scenario diversity SDIV of two scenarios
    no_of_properties = len(prop_diversities)
    diversity_sum = 0
    for prop_diversity in prop_diversities:
        diversity_sum += prop_diversity

    return diversity_sum / no_of_properties


def overall_scenario_diversity(scenario, overall_data, feature_objects):
    """

    :param scenario: scenario to compute diversity metric for
    :param overall_data: dataset
    :param feature_objects: list of features to
    :return: Diversity metric
    """
    # sums the two scenario diversity between scenario
    # and all other scenarios
    overall_scenario_div = 0

    # for each feature, determine the property diversity between the two scenarios
    # for each scenario
    # Preparing SDIV
    all_scenario_property_divs = []
    for i in range(0, len(overall_data.index)):
        # determine the property diversity
        two_scenario_property_divs = []
        if i != scenario:
            for feature in feature_objects:
                two_scenario_property_divs.append(kth_property_diversity(feature.name, scenario, i, overall_data))
            all_scenario_property_divs.append(two_scenario_property_divs)
        # print('two_scenario_property_divs: '+str(two_scenario_property_divs))
    # print('all_scenario_property_divs: '+str(all_scenario_property_divs))

    # sum the two scenario diversity
    two_scenario_diversities = [] # diversity metric between scenario, and all other tests
    # print('len(overall_data.index): '+str(len(overall_data.index)))
    # print('len(feature_objects): ' + str(len(feature_objects)))

    # Computing SDIV for each other scenario
    for i in range(0, len(all_scenario_property_divs)):
        diversity_sum = 0
        for j in range(0, len(feature_objects)):
            # print(j)
            diversity_sum += all_scenario_property_divs[i][j]
        two_scenario_diversities.append(diversity_sum / len(feature_objects))

    print("Scenario " + str(scenario + 1) + " diversity: " + str(round(sum(two_scenario_diversities), 4)) + ", average: " +
          str(round(stats.mean(two_scenario_diversities), 4)))
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

# we want to map the information in each row to a dictionary
# whose keys are are given by a fieldnames parameter
DATA_LIMIT = 20  # limit the data for dev
data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)

# STEPS FOR DIVERSITY CALCS
# 1. normalise the property data so that the values fall between 0 and 1
# 1a. find feature stats
features_strings = ['feature_ego_speed']
feature_objects = feature_stats(data, features_strings)

# 1b. normalise values
normalise_feature_values(data, feature_objects)

# 2. compute scenario diversity for Si with all other scenarios
overall_scenario_diversity(0, data, feature_objects)

# 3. Compute test suite diversity across all scenarios
print("Total suite diversity: " + str(suite_diversity(data, feature_objects)))
