"""
file to read from data from DataSetfeatures.csv and
identify and update incorrect speed classifications
"""
import pandas as pd

# define column headings
speed_heading = 'feature_ego_speed'
speed_demand_heading = 'feature_ego_speedDemand'
speed_label_heading = "feature_ego_speedCategory"
scenario_identifier_heading = "feature_scenarioIdentifier"


class DemandCategory:
    def __init__(self, demand, label):
        self.label = label
        self.demand = demand


# define speed classes
stop_max_speed = 0.01
slow_max_speed = 5
moderate_max_speed = 8


class SpeedCategory(DemandCategory):
    def __init__(self, speed):
        if type(speed) == str:
            print('speed is type: '+str(type(speed)) + ' with value: '+str(speed))

        if 0 <= speed <= stop_max_speed:
            DemandCategory.__init__(self, 1, "Stop (0 < speed (m/s) <= 0.01)")

        elif stop_max_speed < speed <= slow_max_speed:
            DemandCategory.__init__(self, 2, "Slow (0.01 < speed (m/s) <= 5)")

        elif slow_max_speed < speed <= moderate_max_speed:
            DemandCategory.__init__(self, 3, "Moderate (5 < speed (m/s) <= 8)")

        elif moderate_max_speed < speed:
            DemandCategory.__init__(self, 4, "Fast (speed (m/s) > 8)")


def calculate_speed_demand(data):
    # iterate through rows
    for index, row in data.iterrows():

        # extract speed and current demand and label
        speed = row[speed_heading]
        old_demand = row[speed_demand_heading]
        old_label = row[speed_label_heading]

        # generate demand and label
        print('speed: '+str(speed)+' at index: '+str(index))
        category = SpeedCategory(float(speed))
        new_demand = category.demand
        new_label = category.label

        # update if extracted and generated do not match
        if old_demand != new_demand or old_label != new_label:
            data.loc[index, speed_demand_heading] = new_demand
            data.loc[index, speed_label_heading] = new_label

    return data
