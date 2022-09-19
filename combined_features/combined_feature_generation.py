"""
file to add combination features to DataSetfeatures.csv
"""
import pandas as pd
from create_combo_features import *

# read the csv file
DATA_LIMIT = 1000
data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT, index_col=0)

class ComboFeatureInput:
  def __init__(self, label, columnName):
    self.label = label
    self.columnName = columnName
    
weather_combo_inputs = [ComboFeatureInput('rain', 'feature_rainDemand'), 
                        ComboFeatureInput("fog", 'feature_fogDemand'), 
                        ComboFeatureInput("wetness", 'feature_wetnessDemand'),
                        ComboFeatureInput("time", 'feature_timeDemand')]

aggressivness_combo_inputs = [ComboFeatureInput('speed',  'feature_ego_speed'), 
                              ComboFeatureInput("acceleration",'feature_ego_comAcceleration '), 
                              ComboFeatureInput("obstaclesMinDist", 'feature_obstaclesMinimumDistance')]

create_combo_features(weather_combo_inputs, data)
create_combo_features(aggressivness_combo_inputs, data)

print("saving combo features...")
data.to_csv('DataSetfeatures.csv')
