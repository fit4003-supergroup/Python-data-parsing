"""
Running this file will:
- Pre-process data in DataSetfeatures.csv file to
  demand_input.csv and diversity_input.csv files
- Run the demand calculations and output results
  to demand_output.csv file
- Run the diversity calculations and output
  results to diversity_output.csv file
"""

import pandas as pd
import preprocessing
import new_demand_calculations
import new_diversity_calculations

"""
PRE-PROCESSING STEPS
"""
print('\nBeginning Pre-processing ...')
# read the csv file
DATA_LIMIT = 1000  # only reads first 100 rows
data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)

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

processed_demand_features = preprocessing.feature_stats(data, demand_feature_names)

preprocessing.print_to_demand_csv(demand_feature_names, processed_demand_features)

# list features for calculations
diversity_feature_names = [
    'feature_ego_acceleration',
    'feature_ego_speed',
    'feature_totalNPCs',
    'feature_totalPedestrians',
    'feature_totalStaticObstacles',
    'feature_totalRoadUsers',
    'feature_obstaclesAverageDistance',
]

# get feature statistics
processed_diversity_features = preprocessing.feature_stats(data, diversity_feature_names)

# remove outliers from data
preprocessing.remove_outliers(processed_diversity_features)

# normalise data values
preprocessing.normalise_feature_values(processed_diversity_features)

# print results to csv file
preprocessing.print_to_csv(diversity_feature_names, processed_diversity_features)

print('Pre-processing Complete!')

"""
DIVERSITY CALCULATIONS STEPS
"""
print('\nBeginning Diversity Calculations...')

# columns are diversity features and data is normalised
processed_data = pd.read_csv('diversity_input.csv')

# compute diversity
diversities = new_diversity_calculations.compute_diversity(processed_data)

# write to csv
new_diversity_calculations.write_results_to_csv(diversities)
print('Diversity Calculations Complete!')

"""
DEMAND CALCULATIONS STEPS
"""
print('\nBeginning Demand Calculations...')
# read data from input csv
demand_processed_data = pd.read_csv('demand_input.csv')

# get metadata about features
feature_names = list(demand_processed_data.columns)
features = new_demand_calculations.feature_stats(demand_processed_data, feature_names)

# determine the demand values for scenarios
demand_res = new_demand_calculations.scenario_demands(demand_processed_data, features)

# write results to output csv file
new_demand_calculations.write_output_to_csv(demand_res)
print('Demand Calculations Complete!')