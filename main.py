"""
Running this file will:
- Fix missclassification of speed demand
- Generate combination features
- Pre-process data in DataSetfeatures.csv file to
  demand_input.csv and diversity_input.csv files
- Run the demand calculations and output results
  to demand_output.csv file
- Run the diversity calculations and output
  results to diversity_output.csv file
"""

import pandas as pd
import combined_feature_generation
import preprocessing
import demand_calculations
import diversity_calculations
import speed_demand_fix 

"""
READ INPUT FILE
"""
# read the csv file
file_name = 'DataSetfeatures.csv'
modified_file_name = 'DataSetfeatures-modified.csv'
DATA_LIMIT = 10000  # only reads first 10000 rows
print('Reading ' + str(DATA_LIMIT) + " lines from " + file_name)
data = pd.read_csv(file_name, nrows=DATA_LIMIT, index_col=0)

"""
DATA SET MODIFICATION
"""
print('\nRecalculating Speed Demand...')
modified_data = speed_demand_fix.calculate_speed_demand(data)

"""
CALCULATE COMBINATION FEATURES
"""
print('\nCalculating combination features...')
modified_data = combined_feature_generation.calculate_combined_features(modified_data)

print("saving speed demand & combined features...")
modified_data.to_csv(modified_file_name)

"""
PRE-PROCESSING STEPS
"""
print('\nBeginning Pre-processing...')

# read data again 
# need to do this because indexing needs to be different for following steps
data = pd.read_csv(modified_file_name, nrows=DATA_LIMIT)

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
diversities = diversity_calculations.compute_diversity(processed_data)

# write to csv
diversity_calculations.write_results_to_csv(diversities)
print('Diversity Calculations Complete!')

"""
DEMAND CALCULATIONS STEPS
"""
print('\nBeginning Demand Calculations...')
# read data from input csv
demand_processed_data = pd.read_csv('demand_input.csv')

# get metadata about features
feature_names = list(demand_processed_data.columns)
features = demand_calculations.feature_stats(demand_processed_data, feature_names)

# determine the demand values for scenarios
demand_res = demand_calculations.scenario_demands(demand_processed_data, features)

# write results to output csv file
demand_calculations.write_output_to_csv(demand_res)
print('Demand Calculations Complete!')