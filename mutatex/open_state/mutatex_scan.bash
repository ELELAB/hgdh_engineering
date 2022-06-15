#!/usr/bin/bash

# source env
module unload python/3.7/modulefile

# Generate clean pdb without water
pdb_delresname -HOH 1xdw.pdb | pdb_tidy > clean.pdb

# Run mutatex
mutatex clean.pdb --np 4 --foldx-log --foldx-version=suite5 -v  


# Create a separate folder for the mutatex plots
mkdir plots
cp mutation_list plots/
cd plots 

ddg2heatmap -d ../results/mutation_ddgs/clean_model0_checked_Repair -p ../clean_model0_checked.pdb -l mutation_list.txt -n -3.0 -x 5.0 -o final_position

# In case you want only the positions you are interested 
# We manually edited the pdb file to include only them 

ddg2heatmap -d ../results/mutation_ddgs/clean_model0_checked_Repair -p clean_model0_checked.pdb -l mutation_list.txt -n -3.0 -x 5.0 -o specific_position
 
 
