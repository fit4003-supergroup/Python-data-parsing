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
    print('Starting static_dist_comparison')
    manhattan_div = []
    for i in range(len(data.index)):
        manhattan_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'manhattan'), 4))

    euclidean_div = []
    for i in range(len(data.index)):
        euclidean_div.append(round(overall_scenario_diversity(i, data, feature_objects, 'euclidean'), 4))

    SCATTER_CENTRE = 10  # TODO: Make this dynamic to centre of histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

    fig.suptitle('Diversity spread, n = ' + str(len(data)))
    # ax1.scatter(np.full(len(manhattan_div), SCATTER_CENTRE), manhattan_div)
    ax1.hist(manhattan_div, bins='auto', orientation='horizontal', histtype='stepfilled', color='purple')
    ax1.set_xlabel('Number of points')
    ax1.set_title('Manhattan')
    # ax2.scatter(np.full(len(euclidean_div), SCATTER_CENTRE), euclidean_div)
    ax2.hist(euclidean_div, bins='auto', orientation='horizontal', histtype='stepfilled', color='orange')
    ax2.set_title('Euclidean')
    ax2.set_xlabel('Number of points')
    plt.savefig('plots/static_dist.png')


def average_diversity(n_range, feature_objects, data) -> ([int], [int]):
    manhattan_results = []
    euclidean_results = []
    for n in n_range:
        limited_data = data.head(n)
        manhattan_div = []
        for i in range(len(limited_data.index)):
            manhattan_div.append(round(overall_scenario_diversity(i, limited_data, feature_objects, 'manhattan'), 4))

        euclidean_div = []
        for i in range(len(limited_data.index)):
            euclidean_div.append(round(overall_scenario_diversity(i, limited_data, feature_objects, 'euclidean'), 4))

        manhattan_results.append(np.average(manhattan_div))
        euclidean_results.append(np.average(euclidean_div))

    return manhattan_results, euclidean_results


def dynamic_dist_comparison(data, feature_objects):
    """
    Plot the average of diversity metrics against the number of scenarios
    :param data:
    :param feature_objects:
    :return:
    """
    print('Starting dynamic_dist_comparison')
    MIN_N = 50
    MAX_N = 500
    STEP_N = 50
    n_range = np.arange(MIN_N, MAX_N, STEP_N)
    # average values
    manhattan_results, euclidean_results = average_diversity(n_range, feature_objects, data)

    fig = plt.figure(2)
    plt.plot(n_range, manhattan_results, marker='o', label='Manhattan')
    plt.plot(n_range, euclidean_results, color='red', marker='o', label='Euclidean')
    plt.xlabel('Suite size in number of scenarios')
    plt.title('Diversity averages across test suite size')
    plt.legend()
    fig.savefig('plots/dynamic_dist.png')
    pass


def feature_length_comparison(data, feature_objects):
    print('Starting feature_length_comparison')
    MIN_N = 50
    MAX_N = 300
    STEP_N = 25
    n_range = np.arange(MIN_N, MAX_N, STEP_N)

    feature_length_range = np.arange(2, len(feature_objects) + 1, 2)
    fig, axs = plt.subplots(math.ceil(feature_length_range.size / 2), 2)
    plt.subplots_adjust(hspace=0.5)
    ax_flat = []
    for row in axs:
        for col in row:
            ax_flat.append(col)

    for i in range(len(feature_length_range)):
        ax = ax_flat[i]
        features = feature_objects[:feature_length_range[i]]
        manhattan_results, euclidean_results = average_diversity(n_range, features, data)
        ax.plot(n_range, manhattan_results, marker='o', label='Manhattan')
        ax.plot(n_range, euclidean_results, color='red', marker='o', label='Euclidean')
        ax.set_title('feature length = ' + str(len(features)))
        handles, labels = ax.get_legend_handles_labels()
        fig.legend(handles, labels, loc='lower right')
        print('Finished feature_length_comparison subplot ' + str(i+1) + ' of ' + str(len(feature_length_range)))
    fig.suptitle('Diversity average across varying scenario length and feature lengths')
    fig.savefig('plots/feature_length_comparison.png')


if __name__ == '__main__':
    DATA_LIMIT = 3000  # limit the data for dev
    data = pd.read_csv('DataSetfeatures.csv', nrows=DATA_LIMIT)
    features_strings = ['feature_ego_speed', 'feature_ego_acceleration', 'feature_fogDemand', 'feature_obstaclesAverageDistance',
                        'feature_obstaclesAverageVolume', 'feature_obstaclesAverageAcceleration', 'feature_ego_steeringTarget',
                        'feature_collisionProbabilityTimeStamp']
    feature_objects = feature_stats(data, features_strings)
    normalise_feature_values(data, feature_objects)

    static_dist_comparison(data.head(1000), feature_objects[:2])
    dynamic_dist_comparison(data, feature_objects[:2])
    feature_length_comparison(data, feature_objects)

    plt.show()
