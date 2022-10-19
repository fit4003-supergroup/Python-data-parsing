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
import random
import time
import combined_feature_generation
import preprocessing
import demand_calculations
import diversity_calculations
import speed_demand_fix
import categorical_feature_mapping
import quantitative_feature_mapping

"""
READ INPUT FILE
"""
# read the csv file
start = time.perf_counter()
file_name = 'sub-set.csv'
modified_file_name = 'DataSetfeatures-modified.csv'

# get random subset of data from DataSetFeatures.csv
p = 0.05   # fraction of og data to retrieve

# keep_default_na ensures 'null' is read as string and not nan type
"""
data = pd.read_csv(file_name,
                   skiprows=lambda i: i > 0 and random.random() > p,
                   index_col=0, header=0,
                   keep_default_na=False)
data.to_csv('test.csv')
"""

# OLD WAY; select first n rows
#DATA_LIMIT = 100  # only reads first 5000 rows
#print('Reading ' + str(DATA_LIMIT) + " lines from " + file_name)
data = pd.read_csv(file_name,
                   index_col=0,
                   keep_default_na=False)
data.to_csv('test.csv')

"""
DATA SET MODIFICATION
"""
print('\nRecalculating Speed Demand...')
modified_data = speed_demand_fix.calculate_speed_demand(data)

print('\nMapping Categorical Variables to Integer Values...')
modified_data = categorical_feature_mapping.categorical_feature_mapping(modified_data)

print('\nMapping Quantitative Variables to Demand Values...')
modified_data = quantitative_feature_mapping.convert_to_demand(modified_data)

"""
CALCULATE COMBINATION FEATURES
"""
print('\nCalculating combination features...')
modified_data = combined_feature_generation.calculate_combined_features(modified_data)

print("\nSaving modified features...")
modified_data.to_csv(modified_file_name)

"""
PRE-PROCESSING STEPS
"""
print('\nBeginning Pre-processing...')

# read data again
# need to do this because indexing needs to be different for following steps
data = pd.read_csv(modified_file_name)

# demand_feature_names = [
#     'feature_ego_speedDemand',
#     'feature_rainDemand',
#     'feature_fogDemand',
#     'feature_wetnessDemand',
#     'feature_timeDemand',
#     'feature_scenarioTrafficLightDemand',
#     'feature_scenarioSideWalkDemand',
#     'feature_totalNPCs',
#     'feature_totalPedestrians',
#     'feature_totalStaticObstacles',
#     'feature_totalRoadUsers',
#     'feature_obstaclesAverageDistanceDemand',
#     'feature_obstaclesMinimumDistanceDemand',
#     'feature_obstaclesMaximumDistanceDemand',
#     'feature_obstaclesAverageVelocityDemand',
#     'feature_obstaclesMaximumVelocityDemand',
#     'feature_obstaclesMinimumVelocityDemand',
#     'feature_obstaclesAverageAccelerationDemand',
#     'feature_obstaclesMaximumAccelerationDemand',
#     'feature_obstaclesMinimumAccelerationDemand',
#     'feature_ego_operationDemand',
#     'feature_operationOfObstacleHavingMaximumDistanceDemand',
#     'feature_operationOfObstacleHavingMinimumDistanceDemand',
#     'feature_operationOfObstacleHavingMaximumSpeedDemand',
#     'feature_operationOfObstacleHavingMinimumSpeedDemand',
#     'feature_operationOfObstacleHavingMaximumVelocityDemand',
#     'feature_operationOfObstacleHavingMinimumVelocityDemand',
#     'feature_operationOfObstacleHavingMaximumAccelerationDemand',
#     'feature_operationOfObstacleHavingMinimumAccelerationDemand',
#     'feature_operationOfObstacleHavingMaximumVolumeDemand',
#     'feature_operationOfObstacleHavingMinimumVolumeDemand',
#     'feature_combo_rain_fog_wetness_time',
#     'feature_combo_speed_acceleration_obstaclesMinDist'
# ]

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
    'feature_obstaclesMinimumDistanceDemand',
    'feature_obstaclesMaximumDistanceDemand',
    'feature_obstaclesMaximumVelocityDemand',
    'feature_obstaclesMinimumVelocityDemand',
    'feature_obstaclesMaximumAccelerationDemand',
    'feature_obstaclesMinimumAccelerationDemand',
    'feature_ego_operationDemand',
]

processed_demand_features = preprocessing.feature_stats(data, demand_feature_names)
preprocessing.print_to_demand_csv(demand_feature_names, processed_demand_features)

# list features for calculations
diversity_feature_names = [
    'feature_ego_acceleration',
    'feature_ego_throttle',
    'feature_ego_steeringTarget',
    'feature_ego_brake',
    'feature_ego_steeringRate',
    'feature_ego_velocityx',
    'feature_ego_velocityy',
    'feature_ego_accelerationx',
    'feature_ego_accelerationy',
    'feature_ego_accelerationz',
    'feature_ego_positionx',
    'feature_ego_positiony',
    'feature_ego_positionz',
    'feature_ego_operationDemand',
    'feature_rainDemand',
    'feature_fogDemand',
    'feature_wetnessDemand',
    'feature_timeDemand',
    'feature_scenarioTrafficLightDemand',
    'feature_trafficLight',
    'feature_scenarioSideWalkDemand',
    'feature_ego_speed',
    'feature_totalNPCs',
    'feature_totalPedestrians',
    'feature_totalStaticObstacles',
    'feature_totalRoadUsers',
    'feature_obstaclesMaximumDistance',
    'feature_obstaclesMinimumDistance',
    'feature_typeObstacleHavingMaximumDistance',
    'feature_typeObstacleHavingMinimumDistance',
    'feature_obstaclesMaximumSpeed',
    'feature_obstaclesMinimumSpeed',
    'feature_typeObstacleHavingMaximumSpeed',
    'feature_typeObstacleHavingMinimumSpeed',
    'feature_ObstaclesMaximumVelocity',
    'feature_ObstaclesMinimumVelocity',
    'feature_typeObstacleHavingMaximumVelocity',
    'feature_typeObstacleHavingMinimumVelocity',
    'feature_obstaclesMaximumAcceleration',
    'feature_obstaclesMinimumAcceleration',
    'feature_typeObstacleHavingMaximumAcceleration',
    'feature_typeObstacleHavingMinimumAcceleration',
    'feature_obstaclesMaximumVolume',
    'feature_obstaclesMinimumVolume',
    'feature_typeObstacleHavingMaximumVolume',
    'feature_typeObstacleHavingMinimumVolume',
    'feature_volumeObstacleWithMinimumDistance',
    'feature_volumeObstacleWithMaximumSpeed',
    'feature_volumeObstacleWithMaximumVelocity',
    'feature_volumeObstacleWithMaximumAcceleration',
]

# get feature statistics
processed_diversity_features = preprocessing.feature_stats(data, diversity_feature_names)

# remove outliers from data
# preprocessing.remove_outliers(processed_diversity_features)

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

end = time.perf_counter()
print(f"\nProcessing completed in {end - start:0.4f} seconds")
