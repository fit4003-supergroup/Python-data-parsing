
import itertools
import pandas as pd

def normalise_column(column):
    return (column - column.min()) / (column.max() - column.min())

def create_combo_features(inputs, data):
    
    #normalise each input column
    normalisedDf = pd.DataFrame()
    
    for column in inputs:
        normalisedDf[column.columnName] = normalise_column(data[column.columnName])
    
    # generate combo feature
    for i in range(2, len(inputs) + 1):
        for combo in itertools.combinations(inputs, i):
            
            columnNames = []
            labels = []
            for feature in combo:
                columnNames.append(feature.columnName)
                labels.append(feature.label)
            
            comboColumnName = "feature_combo_" + "_".join(labels)
            
            # save to dataframe
            data[comboColumnName] = normalisedDf[columnNames].mean(axis=1)