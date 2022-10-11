import pandas as pd
import csv
from scipy.stats import spearmanr
from scipy.stats import pearsonr

data = pd.read_csv('demand_input_with_collisionDemand.csv')

class Feature:
    def __init__(self, name, spearman_correlation, spearman_pvalue, pearson_correlation, pearson_pvalue) -> None:
        self.name = name
        self.spearman_correlation = spearman_correlation
        self.spearman_pvalue = spearman_pvalue
        self.pearson_correlation = pearson_correlation
        self.pearson_pvalue = pearson_pvalue

def feature_stats(overall_data):
    feature_objects = []
    for column in overall_data:
        # calculate correlation with collisionProbability

        spear_corr, spear_pvalue = spearmanr(overall_data[column], overall_data["feature_collisionEventDemand"],
                                             nan_policy="omit")
        pears_corr, pears_pvalue = pearsonr(overall_data[column], overall_data["feature_collisionEventDemand"])

        # create object to store
        feature_objects.append(Feature(column, spear_corr, spear_pvalue, pears_corr, pears_pvalue))

    return feature_objects

correlation_features = feature_stats(data)
feature_correlations = []

def write_to_csv(correlation_features):
    # open csv file in write mode
    with open('demand_collision_event_correlation_new.csv', 'w') as file:
        # create csv writer
        writer = csv.writer(file)
        writer.writerow(
            ['demand feature name', 'spearman correlation', 'spearman pvalue', 'pearson correlation',
             'pearson pvalue'])
        # write rows to file
        for i in range(0, len(correlation_features)):
            feature_correlations.append([correlation_features[i].name, correlation_features[i].spearman_correlation,
                                         correlation_features[i].spearman_pvalue,
                                         correlation_features[i].pearson_correlation,
                                         correlation_features[i].pearson_pvalue])
            writer.writerow([correlation_features[i].name, correlation_features[i].spearman_correlation,
                             correlation_features[i].spearman_pvalue,
                             correlation_features[i].pearson_correlation, correlation_features[i].pearson_pvalue])


write_to_csv(correlation_features)
