# code to parse and analyse features from DataSetfeatures file
# *note: assumes file 'DataSetFeatures.csv' is in same folder
import pandas as pd
import csv

# calculates demand value for a given scenario
def feature_demand(scenario, feature):
    # Returns 1 if high demand feature value
    # Returns 0 if not high demand feature value

    # compare to scenario demand value
    feature_value = scenario[feature.name]
    # if > medium then high demand
    if feature_value > feature.medium_demand:
        print(str(feature.name) + ' is demanding for scenario ')
        return 1
    else:  # if < medium then low demand
        print(str(feature.name) + ' is not demanding for scenario ')
        return 0


def scenario_demand(scenario_num, overall_data, features_list):
    # calculates the demand for the given scenario
    scenario = overall_data.iloc[scenario_num]
    scenario_id = scenario['feature_scenarioIdentifier']

    print("\n*********************************")
    print("CALCULATING SCENARIO " + str(scenario_id) + " DEMAND ...")
    print("*********************************")

    demand_sum = 0
    # for each feature in the feature set, find whether the value is high demand
    # add demand value to demand_sum - most demanding scenarios will have highest sum
    for feature in features_list:
        demand_sum += feature_demand(scenario, feature)

    print('\nOverall scenario demand is ' + str(demand_sum))
    return demand_sum


class Feature:
    # object to store feature info
    def __init__(self, name, medium_demand):
        self.name = name
        self.medium_demand = medium_demand


def feature_stats(overall_data, feature_set):
    # determines the min, max and medium for
    # each of the features
    # creates a feature object and returns
    print("*********************************")
    print("CALCULATING FEATURE STATISTICS...")
    print("*********************************")
    feature_objects = []
    for feature in feature_set:
        feature_min = min(overall_data[feature])
        feature_max = max(overall_data[feature])
        medium_demand = (feature_max - feature_min) / 2
        feature_objects.append(Feature(feature, medium_demand))

    for feature in feature_objects:
        print('\nfeature name: ' + str(feature.name))
        print('feature medium: ' + str(feature.medium_demand))

    return feature_objects


def scenario_demands(no_of_scenarios, overall_data, features_list):
    # calculates the demand values for the first n scenarios
    # where n is no_of_scenarios
    demands = []
    for i in range(0, no_of_scenarios):
        demands.append(scenario_demand(i, overall_data, features_list))

    for i in range(0, len(demands)):
        print('scenario: '+str(i)+', demand: '+str(demands[i]))

    return demands


def write_to_csv(demand_results):
    # open csv file in write mode
    with open('demand_output.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['scenario no.', 'scenario demand'])
        # write rows to file
        for i in range(0, len(demand_results)):
            writer.writerow([i, demand_results[i]])


# 1. we want to map the information in each row to a dictionary
# whose keys are are given by a fieldnames parameter
data = pd.read_csv('DataSetfeatures.csv')

# 2. list desired demand features
features_names = ['feature_ego_speedDemand', 'feature_rainDemand', 'feature_fogDemand', 'feature_wetnessDemand',
                  'feature_timeDemand', 'feature_scenarioTrafficLightDemand', 'feature_scenarioSideWalkDemand']
# 3. find the feature's min, max, and demand
features = feature_stats(data, features_names)

# 4. find the demand for overall scenario
# * not currently calculating for 60,000
demand_res = scenario_demands(60000, data, features)

# 5. write to csv
write_to_csv(demand_res)
