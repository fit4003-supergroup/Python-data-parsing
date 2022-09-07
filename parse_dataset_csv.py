# code to parse and analyse features from DataSetfeatures file
# *note: assumes file 'DataSetFeatures.csv' is in same folder
import pandas as pd
import math

# we want to map the information in each row to a dictionary
# whose keys are are given by a fieldnames parameter
data = pd.read_csv('DataSetfeatures.csv')


# calculates demand value for a given scenario
def scenario_demand(overall_data, feature_name):
    scenario = overall_data.iloc[0]
    scenario_id = scenario['feature_scenarioIdentifier']

    print('calculating demand for scenario ' + str(scenario_id))
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
        print(str(feature_name) + ' is demanding for scenario ' + str(scenario_id))
    else:  # if < medium then low demand
        print(str(feature_name) + ' is not demanding for scenario ' + str(scenario_id))


scenario_demand(data, 'feature_ego_speedDemand')
