from asyncore import write
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile
import pandas as pd
import csv
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import statistics

class Feature:
    def __init__(self, name, spearman_correlation, spearman_pvalue, pearson_correlation, pearson_pvalue, data_values) -> None:
        self.name = name
        self.spearman_correlation = spearman_correlation
        self.spearman_pvalue = spearman_pvalue
        self.data_values = data_values
        self.pearson_correlation = pearson_correlation
        self.pearson_pvalue = pearson_pvalue        

def feature_stats(overall_data, feature_set):
    feature_objects = []
    for feature in feature_set:
        # get values
        data_values = []
        for i in range(0, len(overall_data[feature])):
            data_values.append(overall_data[feature][i])

        # calculate correlation with collisionProbability

        spear_corr, spear_pvalue = spearmanr(overall_data[feature], overall_data["feature_collisionEventDemand"], nan_policy="omit")
        pears_corr, pears_pvalue = pearsonr(overall_data[feature], overall_data["feature_collisionEventDemand"])

        # create object to store
        feature_objects.append(Feature(feature, spear_corr, spear_pvalue, pears_corr, pears_pvalue, data_values))

    return feature_objects



# def standardised_feature_stats(overall_data, feature_set):
#     feature_objects = []
#     for feature in feature_set:
#         # get values
#         data_values = []
#         for i in range(0, len(overall_data[feature])):
#             data_values.append(overall_data[feature][i])

#         mean_data = mean(data_values)
#         sd_data = statistics.stdev(data_values)

#         for i in range(0, len(data_values)):
#             data_values[i] = (data_values[i] - mean_data)/sd_data

#         # calculate correlation with collisionProbability

#         spear_corr, spear_pvalue = spearmanr(data_values, overall_data["feature_collisionProbability"], nan_policy="omit")
#         pears_corr, pears_pvalue = pearsonr(data_values, overall_data["feature_collisionProbability"])

#         # create object to store
#         feature_objects.append(Feature(feature, spear_corr, spear_pvalue, pears_corr, pears_pvalue, data_values))

#     return feature_objects

# read the csv file
data = pd.read_csv('DataSetfeatures.csv')

correlation_feature_names = [
    "feature_ego_acceleration",
    "feature_ego_throttle",
    "feature_ego_steeringTarget",
    "feature_ego_brake",
    "feature_ego_steeringRate",
    "feature_ego_speed",
    "feature_ego_speedDemand",
    "feature_ego_velocityx",
    "feature_ego_velocityy",
    "feature_ego_comVelocity",
    "feature_ego_accelerationx",
    "feature_ego_accelerationy",
    "feature_ego_accelerationz",
    "feature_ego_comAcceleration",
    "feature_ego_positionx",
    "feature_ego_positiony",
    "feature_ego_positionz",
    "feature_ego_comPosition",
    "feature_rainDemand",
    "feature_fogDemand",
    "feature_wetnessDemand",
    "feature_timeDemand",
    "feature_trafficLight",
    "feature_scenarioSideWalkDemand",
    "feature_totalNPCs",
    "feature_totalPedestrians",
    "feature_totalStaticObstacles",
    "feature_totalRoadUsers",
    "feature_obstaclesAverageDistance",
    "feature_obstaclesMaximumDistance",
    "feature_obstaclesMinimumDistance",
    "feature_typeObstacleHavingMaximumDistance",
    "feature_typeObstacleHavingMinimumDistance",
    # "feature_obstaclesAverageSpeed",
    "feature_obstaclesMaximumSpeed",
    "feature_obstaclesMinimumSpeed",
    "feature_typeObstacleHavingMaximumSpeed",
    "feature_typeObstacleHavingMinimumSpeed",
    # "feature_ObstaclesAverageVelocity",
    "feature_ObstaclesMaximumVelocity",
    "feature_ObstaclesMinimumVelocity",
    "feature_typeObstacleHavingMaximumVelocity",
    "feature_typeObstacleHavingMinimumVelocity",
    # "feature_obstaclesAverageAcceleration",
    "feature_obstaclesMaximumAcceleration",
    "feature_obstaclesMinimumAcceleration",
    "feature_typeObstacleHavingMaximumAcceleration",
    "feature_typeObstacleHavingMinimumAcceleration",
    "feature_obstaclesAverageVolume",
    "feature_obstaclesMaximumVolume",
    "feature_obstaclesMinimumVolume",
    "feature_typeObstacleHavingMaximumVolume",
    "feature_typeObstacleHavingMinimumVolume",
    "feature_volumeObstacleWithMinimumDistance",
    "feature_volumeObstacleWithMaximumSpeed",
    "feature_volumeObstacleWithMaximumVelocity",
    "feature_volumeObstacleWithMaximumAcceleration",
    "feature_collisionEventDemand",
    "feature_collisionProbabilityTimeStamp"
]


correlation_features = feature_stats(data, correlation_feature_names)
feature_correlations = []

def write_to_csv(correlation_features):  
    # open csv file in write mode
    with open('correlation_output_collision_event.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(['feature name', 'spearman feature correlation', 'spearman feature pvalue', 'pearson feature correlation', 'pearson pvalue'])
        # write rows to file
        for i in range(0, len(correlation_features)):
            feature_correlations.append([correlation_features[i].name, correlation_features[i].spearman_correlation, correlation_features[i].spearman_pvalue, 
            correlation_features[i].pearson_correlation, correlation_features[i].pearson_pvalue])
            writer.writerow([correlation_features[i].name, correlation_features[i].spearman_correlation, correlation_features[i].spearman_pvalue, 
            correlation_features[i].pearson_correlation, correlation_features[i].pearson_pvalue])

write_to_csv(correlation_features)
