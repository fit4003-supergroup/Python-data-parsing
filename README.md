# Python-data-parsing
Storing files for parsing, cleaning and calculating data from the dataset in python

Note:
- Current code assumes you have file `DataSetfeatures.csv` located in the same directory; check that the row names match those described in the code. 

`main.py`:
- This file calls functions from `preprocessing.y` to pre-process the data from
 `DataSetfeatures.csv`, write to the `diversity_input.csv` and `demand_input.csv` files. 
- Functions are then called from `demand_calculations.py`, and `diversity_calculations.py` 
  which read the data from the input files and compute the relevant calculations before
  writing the results to the `demand_output.csv` and `diversity_output.csv` files respectively.

`speed_demand_fix.py`
- This file identifies and updates incorrect speed classifications in the 
  `DataSetfeatures.csv` file.
- This should be run only once before `main.py`.