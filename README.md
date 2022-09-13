# Python-data-parsing
Storing files for parsing, cleaning and calculating data from the dataset in python

Note:
- Current code assumes you have file `DataSetfeatures.csv` located in the same directory; check that the row names match those described in the code. 

`preprocessing.py` :
- Running this file will process the raw data and write the output to two files
- The demand data will be written to `demand_input.csv` for use in demand calculations.
- The diversity data will be written to `diversity_input.csv` for use in diversity calculations.

`demand_calculations.py` :
- Running this file will carry out the demand calculations on the selected dataset features
- This will print the results to a `demand_output.csv` file in the same folder.

`diversity_calculations.py` :
- Running this file will carry out the diversity calculations on the selected dataset features
- This will print the results to a `diversity_output.csv` file in the same folder.