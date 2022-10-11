import os
import sys
import re
import demand_calculations
import diversity_calculations


def consolidate_results(n: int):
    parent_path = os.path.abspath(os.path.dirname(__file__))
    all_results = os.listdir(parent_path + '\\results')
    diversity_files = []
    demand_files = []
    for res in all_results:
        if str(n) in res:
            if 'demand' in res:
                demand_files.append(res)
            elif 'diversity' in res:
                diversity_files.append(res)

    # shouldn't be necessary
    diversity_files.sort()
    demand_files.sort()

    concatenated_diversity = []
    for div_file in diversity_files:
        with open('results\\' + div_file, 'r') as file:
            file.readline()  # header
            file.readline()  # blank
            toggle = True
            for line in file:
                if toggle:
                    scenario, diversity = line.replace('\n', '').split(',')
                    concatenated_diversity.append([int(scenario), float(diversity)])
                toggle = not toggle

    concatenated_demand = []
    demand_features = []
    for dem_file in demand_files:
        with open('results\\' + dem_file, 'r') as file:
            columns = file.readline().replace('\n','').split(',')  # header
            demand_features = columns[1:]
            if (len(concatenated_demand) == 0):
                for _ in demand_features:
                    concatenated_demand.append([])
            file.readline()  # blank

            toggle = True
            for line in file:
                if toggle:
                    cols = line.replace('\n', '').split(',')
                    scenario = int(cols[0])
                    demands = [int(n) for n in cols[1:]]
                    for i in range(len(demands)):
                        concatenated_demand[i].append(demands[i])
                toggle = not toggle
    demand_calculations.write_output_to_csv(concatenated_demand, demand_features, filename='results\\demand_output' + str(n) + '-A.csv')
    diversity_calculations.write_results_to_csv(concatenated_diversity, 'results\\diversity_output' + str(n) + '-A.csv')
    print('Output consolidated')


if __name__ == '__main__':
    try:
        consolidate_results(int(sys.argv[1]))
    except:
        consolidate_results(8000)
