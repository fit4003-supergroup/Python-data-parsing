"""
This file maps features with quantitative values from DataSetfeatures.csv
into corresponding integer representations for demand calculations
"""
import pandas as pd

distance_feature_names = [
    'feature_obstaclesAverageDistance',
    'feature_obstaclesMaximumDistance',
    'feature_obstaclesMinimumDistance',
]

velocity_feature_names = [
    'feature_ObstaclesAverageVelocity',
    'feature_ObstaclesMaximumVelocity',
    'feature_ObstaclesMinimumVelocity'
]

acceleration_feature_names = [
    'feature_obstaclesAverageAcceleration',
    'feature_obstaclesMaximumAcceleration',
    'feature_obstaclesMinimumAcceleration'
]


def get_distance_demand(distance_value):
    """
    converts the distance value in meters
    to corresponding demand value
    :param distance_value:
    :return:
    """
    if distance_value == 0:
        return 6
    elif 0 < distance_value <= 5:
        return 5
    elif 5 < distance_value <= 10:
        return 4
    elif 10 < distance_value <= 20:
        return 3
    elif 20 < distance_value <= 40:
        return 2
    elif 40 < distance_value <= 60:
        return 1
    else:
        return 0


def get_velocity_demand(velocity_value):
    """
    converts the velocity value in m/s
    to corresponding demand value
    :param velocity_value:
    :return:
    """
    if not isinstance(velocity_value, int):
        velocity_value = float(velocity_value)

    if velocity_value > 35:
        return 7
    elif 30 < velocity_value <= 35:
        return 6
    elif 25 < velocity_value <= 30:
        return 5
    elif 20 < velocity_value <= 25:
        return 4
    elif 15 < velocity_value <= 20:
        return 3
    elif 10 < velocity_value <= 15:
        return 2
    elif 0 < velocity_value <= 10:
        return 1
    else:
        return 0


def get_acceleration_value(acceleration_value):
    """
    converts the acceleration value in m/s^2
    to corresponding demand value
    :param acceleration_value:
    :return:
    """
    if not isinstance(acceleration_value, int):
        acceleration_value = float(acceleration_value)

    if acceleration_value > 15:
        return 6
    elif 12 < acceleration_value <= 15:
        return 5
    elif 9 < acceleration_value <= 12:
        return 4
    elif 6 < acceleration_value <= 9:
        return 3
    elif 3 < acceleration_value <= 6:
        return 2
    elif 0 < acceleration_value <= 3:
        return 1
    else:
        return 0


def convert_to_demand(data):
    """
    Converts distance, velocity and acceleration data values
    into corresponding demand values to be used in demand
    calculations (adds new columns)
    :param data: Pandas DataFrame read from csv file
    :return:
    """
    # columns to add to dataframe
    dist_avg = []
    dist_min = []
    dist_max = []
    vel_avg = []
    vel_min = []
    vel_max = []
    acc_avg = []
    acc_min = []
    acc_max = []

    # iterate through the rows
    for index, row in data.iterrows():
        for feature_name in distance_feature_names:
            # get current distance value
            dist_val = row[feature_name]
            # find new demand value
            dist_demand_val = get_distance_demand(dist_val)
            if feature_name == distance_feature_names[0]:
                dist_avg.append(dist_demand_val)
            elif feature_name == distance_feature_names[1]:
                dist_max.append(dist_demand_val)
            elif feature_name == distance_feature_names[2]:
                dist_min.append(dist_demand_val)

        for feature_name in velocity_feature_names:
            # get current velocity value
            vel_value = row[feature_name]
            # find new demand value
            vel_demand_val = get_velocity_demand(vel_value)
            if feature_name == velocity_feature_names[0]:
                vel_avg.append(vel_demand_val)
            elif feature_name == velocity_feature_names[1]:
                vel_max.append(vel_demand_val)
            elif feature_name == velocity_feature_names[2]:
                vel_min.append(vel_demand_val)

        for feature_name in acceleration_feature_names:
            # get current acceleration value
            acc_value = row[feature_name]
            # find new demand value
            acc_demand_val = get_acceleration_value(acc_value)
            if feature_name == acceleration_feature_names[0]:
                acc_avg.append(acc_demand_val)
            elif feature_name == acceleration_feature_names[1]:
                acc_max.append(acc_demand_val)
            elif feature_name == acceleration_feature_names[2]:
                acc_min.append(acc_demand_val)

    # add new columns with demand values
    data['feature_obstaclesAverageDistanceDemand'] = dist_avg
    data['feature_obstaclesMaximumDistanceDemand'] = dist_max
    data['feature_obstaclesMinimumDistanceDemand'] = dist_min
    data['feature_obstaclesAverageVelocityDemand'] = vel_avg
    data['feature_obstaclesMaximumVelocityDemand'] = vel_max
    data['feature_obstaclesMinimumVelocityDemand'] = vel_min
    data['feature_obstaclesAverageAccelerationDemand'] = acc_avg
    data['feature_obstaclesMaximumAccelerationDemand'] = acc_max
    data['feature_obstaclesMinimumAccelerationDemand'] = acc_min

    return data
