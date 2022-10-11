"""
file to add combination features to DataSetfeatures.csv
"""
import pandas as pd
from create_combo_features import *

class ComboFeatureInput:
  def __init__(self, label, columnName):
    self.label = label
    self.columnName = columnName

def calculate_combined_features(data):
    
    weather_combo_inputs = [ComboFeatureInput('rain', 'feature_rainDemand'), 
                            ComboFeatureInput("fog", 'feature_fogDemand'), 
                            ComboFeatureInput("wetness", 'feature_wetnessDemand'),
                            ComboFeatureInput("time", 'feature_timeDemand')]

    aggressivness_combo_inputs = [ComboFeatureInput('speed',  'feature_ego_speed'), 
                                ComboFeatureInput("acceleration",'feature_ego_comAcceleration'), 
                                ComboFeatureInput("obstaclesMinDist", 'feature_obstaclesMinimumDistance')]

    print("calculating weather features...")
    create_combo_features(weather_combo_inputs, data)
    
    print("calculating aggressiveness features...")
    create_combo_features(aggressivness_combo_inputs, data)

    return data
