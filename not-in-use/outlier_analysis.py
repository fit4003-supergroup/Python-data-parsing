"""
USED FOR RESEARCH PURPOSES
file to read from data from DataSetfeatures.csv and
identify outliers in the data.
"""
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
from numpy import percentile
import pandas as pd

# read data from csv
DATA_LIMIT = 10000  # limit the data for dev
data = pd.read_csv('../DataSetfeatures.csv', nrows=DATA_LIMIT)

# define features
feature_name = 'feature_ego_speed'

###################################################
#           STANDARD DEVIATION METHOD             #
###################################################
"""
used if the values of the distribution are gaussian
or gaussian-like.
"""
print('\nSTDEV METHOD...')
# get values
stedv_values = []
for i in range(0, len(data[feature_name])):
    stedv_values.append(data[feature_name][i])
print(stedv_values)

# find mean and std
data_mean, data_std = mean(stedv_values), std(stedv_values)

# find outliers and remove
# define lower and upper bounds
cutoff = 3 * data_std
lower, upper = data_mean - cutoff, data_mean + cutoff
print('lower: '+str(lower)+', upper: '+str(upper))

# find outliers
outliers = [x for x in stedv_values if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))

# remove outliers
outliers_removed = [x for x in stedv_values if lower <= x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))

###################################################
#                   IQR METHOD                    #
###################################################
"""
used if the data is not normal enough to be treated
as being drawn from a gaussian distribution
"""
print('\nIQR METHOD...')
# get values
iqr_values = []
for i in range(0, len(data[feature_name])):
    iqr_values.append(data[feature_name][i])
print(iqr_values)

# define interquartile range
q25, q75 = percentile(iqr_values, 25), percentile(iqr_values, 75)
iqr = q75 - q25

# determine outlier cutoff
iqr_cutoff = iqr*1.5
iqr_lower, iqr_upper = q25 - iqr_cutoff, q75 + iqr_cutoff

# identify outliers
iqr_outliers = [y for y in iqr_values if y < iqr_lower or y > iqr_upper]
print('Identified outliers: %d' % len(iqr_outliers))

# remove outliers
iqr_outliers_removed = [y for y in iqr_values if lower <= y <= upper]
print("Non-outlier observations: %d" % len(iqr_outliers_removed))
