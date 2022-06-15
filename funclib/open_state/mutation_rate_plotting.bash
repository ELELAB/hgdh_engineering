#!/usr/bin/bash


# scan 1

python3 funclib_plot.py -i scan1/best_clustered_mutants.csv -seq  -b -o scan1/scan1_1xdw_open

# scan 2

python3 funclib_plot.py -i scan2/best_clustered_mutants.csv -seq  -b -o scan2/scan2_1xdw_open

# scan 3

python3 funclib_plot.py -i scan3/best_clustered_mutants.csv -seq  -b -o scan3/scan3_1xdw_open

