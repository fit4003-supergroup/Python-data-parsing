"""
This file maps categorical features from DataSetfeatures.csv into
corresponding integer representations for demand calculations
"""

# for each categorical feature
# read through column values
# if value is <category> then assign <category_int>

categorical_feature_names = [
    'feature_ego_operation',
    'feature_operationOfObstacleHavingMaximumDistance',
    'feature_operationOfObstacleHavingMinimumDistance',
    'feature_operationOfObstacleHavingMaximumSpeed',
    'feature_operationOfObstacleHavingMinimumSpeed',
    'feature_operationOfObstacleHavingMaximumVelocity',
    'feature_operationOfObstacleHavingMinimumVelocity',
    'feature_operationOfObstacleHavingMaximumAcceleration',
    'feature_operationOfObstacleHavingMinimumAcceleration',
    'feature_operationOfObstacleHavingMaximumVolume',
    'feature_operationOfObstacleHavingMinimumVolume',
]

ego_operation_values = {
    'Stop': 0,
    'ChangeLaneToLeft': 1,
    'ChangeLaneToRight': 2,
    'SpeedUp': 3,
    'SpeedCut': 4,
    'EmergencyBrake': 5,
    'TurnRight': 6,
    'TurnLeft': 7,
    'Cruise': 8
}

obstacle_operation_values = {
    'null': 0,
    'SwitchLane (RightToLeft)': 1,
    'SwitchLane (LeftToRight)': 2,
    'Crossing the road (left to right)': 3,
    'Crossing the road (right to left)': 4,
    'StandOnFrontLane': 5,
    'MaintainLane': 6,
    'FrontLaneWalking': 7,
    'lyingStill': 8,
    'TurnRight': 9
}


def categorical_feature_mapping(data):
    # columns to add to dataframe
    ego = []
    max_dist = []
    min_dist = []
    max_speed = []
    min_speed = []
    max_vel = []
    min_vel = []
    max_acc = []
    min_acc = []
    max_vol = []
    min_vol = []

    for index, row in data.iterrows():
        for feature_name in categorical_feature_names:
            # get current category
            category = row[feature_name]
            # get new value
            new_value = 0
            if feature_name == 'feature_ego_operation':
                # find corresponding ego value
                new_value = ego_operation_values[category]
            else:
                # find corresponding obstacle value
                new_value = obstacle_operation_values[category]

            # update value in data
            data.loc[index, feature_name] = new_value
            if feature_name == categorical_feature_names[0]:
                ego.append(new_value)
            elif feature_name == categorical_feature_names[1]:
                max_dist.append(new_value)
            elif feature_name == categorical_feature_names[2]:
                min_dist.append(new_value)
            elif feature_name == categorical_feature_names[3]:
                max_speed.append(new_value)
            elif feature_name == categorical_feature_names[4]:
                min_speed.append(new_value)
            elif feature_name == categorical_feature_names[5]:
                max_vel.append(new_value)
            elif feature_name == categorical_feature_names[6]:
                min_vel.append(new_value)
            elif feature_name == categorical_feature_names[7]:
                max_acc.append(new_value)
            elif feature_name == categorical_feature_names[8]:
                min_acc.append(new_value)
            elif feature_name == categorical_feature_names[9]:
                max_vol.append(new_value)
            elif feature_name == categorical_feature_names[10]:
                min_vol.append(new_value)

    # add new columns with demand values
    data['feature_ego_operationDemand'] = ego
    data['feature_operationOfObstacleHavingMaximumDistanceDemand'] = max_dist
    data['feature_operationOfObstacleHavingMinimumDistanceDemand'] = min_dist
    data['feature_operationOfObstacleHavingMaximumSpeedDemand'] = max_speed
    data['feature_operationOfObstacleHavingMinimumSpeedDemand'] = min_speed
    data['feature_operationOfObstacleHavingMaximumVelocityDemand'] = max_vel
    data['feature_operationOfObstacleHavingMinimumVelocityDemand'] = min_vel
    data['feature_operationOfObstacleHavingMaximumAccelerationDemand'] = max_acc
    data['feature_operationOfObstacleHavingMinimumAccelerationDemand'] = min_acc
    data['feature_operationOfObstacleHavingMaximumVolumeDemand'] = max_vol
    data['feature_operationOfObstacleHavingMinimumVolumeDemand'] = min_vol
    return data

