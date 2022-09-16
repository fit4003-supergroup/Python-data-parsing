import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from diversity_calculations import *


def static_dist_comparison(data, feature_objects):
    """
    Plots two diversity spreads for the same dataset using both euclidean and manhattan distance.
    Use scatterplot and histogram
    :param data:
    :param feature_objects:
    :return:
    """
    manhattan_div = []
    for i in range(len(data.index)):
        manhattan_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'manhattan'), 4))

    euclidean_div = []
    for i in range(len(data.index)):
        euclidean_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'euclidean'), 4))

    SCATTER_CENTRE = 10  # TODO: Make this dynamic to centre of histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    fig.suptitle('Diversity spread, n = ' + str(len(data)))
    ax1.scatter(np.full(len(manhattan_div), SCATTER_CENTRE), manhattan_div)
    ax1.hist(manhattan_div, bins='auto', orientation='horizontal', histtype='step', color='orange')
    ax1.set_title('Manhattan')
    ax2.scatter(np.full(len(euclidean_div), SCATTER_CENTRE), euclidean_div)
    ax2.hist(euclidean_div, bins='auto', orientation='horizontal', histtype='step', color='orange')
    ax2.set_title('Euclidean')
    plt.show()


if __name__ == '__main__':
    DATA_LIMIT = 1000  # limit the data for dev
    data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)
    features_strings = ['feature_ego_speed', 'feature_ego_acceleration']
    feature_objects = feature_stats(data, features_strings)
    normalise_feature_values(data, feature_objects)
    static_dist_comparison(data.head(100), feature_objects)
