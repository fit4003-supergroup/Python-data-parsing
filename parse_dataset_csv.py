# code to parse and analyse features from DataSetfeatures file
# *note: assumes file 'DataSetFeatures.csv' is in same folder
import pandas as pd

# we want to map the information in each row to a dictionary
# whose keys are are given by a fieldnames parameter
data = pd.read_csv('DataSetfeatures.csv')


# calculates demand value for a given scenario
def feature_demand(scenario, overall_data, feature_name):
    # Returns 1 if high demand feature value
    # Returns 0 if not high demand feature value

    # find min demand for feature
    feature_min = min(overall_data[feature_name])
    print('min: '+str(feature_min))
    # find max demand for feature
    feature_max = max(overall_data[feature_name])
    print('max: '+str(feature_max))
    # calculate medium, e.g. (max-min)/2
    feature_medium = (feature_max - feature_min) / 2
    # compare to scenario demand value
    # if > medium then high demand
    feature_value = scenario[feature_name]
    print('medium: '+str(feature_medium))
    print('value: '+str(feature_value))
    if feature_value > feature_medium:
        print(str(feature_name) + ' is demanding for scenario ')
        return 1
    else:  # if < medium then low demand
        print(str(feature_name) + ' is not demanding for scenario ')
        return 0


def scenario_demand(scenario_num, overall_data, feature_set):
    scenario = overall_data.iloc[scenario_num]
    scenario_id = scenario['feature_scenarioIdentifier']
    print('calculating demand for scenario ' + str(scenario_id))

    demand_sum = 0
    # for each feature in the feature set, find whether the value is high demand
    # add demand value to demand_sum - most demanding scenarios will have highest sum
    for feature in feature_set:
        print('\nfinding demand for feature '+str(feature))
        demand_sum += feature_demand(scenario, overall_data, feature)

    print('\nOverall scenario demand is '+str(demand_sum))


demand_features = ['feature_ego_speedDemand', 'feature_rainDemand', 'feature_fogDemand', 'feature_wetnessDemand',
                   'feature_timeDemand', 'feature_scenarioTrafficLightDemand', 'feature_scenarioSideWalkDemand']
scenario_demand(0, data, demand_features)
# DEMAND FEATURES
# 'feature_ego_speedDemand'
# 'feature_rainDemand'
# 'feature_fogDemand'
# 'feature_wetnessDemand'
# 'feature_timeDemand'
# 'feature_scenarioTrafficLightDemand'
# 'feature_scenarioSideWalkDemand'
