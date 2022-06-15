#!/usr/bin/env python3


from pathlib import Path
import MDAnalysis as mda
import numpy as np
import math
import os, sys
from optparse import OptionParser
from collections import OrderedDict
import argparse
import shutil
import logomaker
import pandas 
import matplotlib.pyplot as plt


def barplot(l,title,out):
    
    
    d = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
         'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
         'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
         'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    
    d1 = {'A':'Ala','G':'Gly','I':'Ile','L':'Leu','P':'Pro','V':'Val',   # aliphatic
           'F':'Phe','W':'Trp','Y':'Tyr',#aromatic
           'D':'Asp','E':'Glu',# negative charged
           'R':'Arg','H':'His','K':'Lys', # positive charged
           'S':'Ser','T':'Thr', # hydroxylic
           'C':'Cys','M':'Met', # sulfur
           'N':'Asn','Q':'Gln' }   
 
    res = ['A','G','I','L','P','V',   # aliphatic
           'F','W','Y', # aromatic
           'D','E',# negative charged
           'R','H','K', # positive charged
           'S','T', # hydroxylic
           'C','M', # sulfur
           'N','Q'] # amidic

    colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4',
              '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff',
              '#9a6324', '#ffffff', '#800000', '#aaffc3', '#808000', '#323232',
              '#000075', '#cccccc' ]

    d_color = {} 
    for i in range(len(res)):
        d_color[res[i]] = colors[i]
    
  
    data = pandas.DataFrame()
    c = []
    for column in l.drop("total_score",axis= 1):
        data = data.append(l[column].value_counts())
        c.append(int(column.strip('A')))
    data.index  = c
    c = list(map(str, c))
    l1 = l.drop("total_score",axis= 1).iloc[0].tolist()
    label = [l1[i]+c[i] for i in range(len(l1))]
    data = data.divide(len(l)).multiply(100) # percentage per column
  
    s = set(data.columns.values.tolist())
    missing_res = [x for x in res if x not in s]
    for res in missing_res:
    	data[res] = np.nan
    data = data.fillna(0) 
    data = data[['A','G','I','L', 'P', 'V', 'F', 'W', 'Y', 'D', 'E', 'R',
                 'H', 'K', 'S', 'T', 'C', 'M', 'N', 'Q']]
   
    # Plotting
    data.plot.bar(color=[d_color.get(x, '#333333') for x in data.columns], 
                  stacked=True, 
                  figsize=(10,7),
                  edgecolor='black',
                  alpha=0.85)
    plt.legend(loc='upper left', 
               bbox_to_anchor=(1,1), 
               ncol=1) 
    # Get locations and labels
    locs, labels = plt.xticks()   
    plt.title(title)         
    plt.xticks([i for i in range(len(label))],label )
    plt.savefig(out+"_barplot.pdf",dpi=300)
    
    

def logos(l,out):
    

    data = pandas.DataFrame()
    c = []
    for column in l.drop("total_score",axis= 1):
        data = data.append(l[column].value_counts())
        c.append(int(column.strip('A')))
    data.index  = range(len(c))
    data = data.divide(len(l)).multiply(100) # percentage per column
    data = data.fillna(0)
    logo = logomaker.Logo(data,shade_below=.5,fade_below=.5,color_scheme='chemistry')
    logo.style_spines(spines=['left', 'right'], visible=False)
    logo.ax.set_xticks(range(len(data)))
    logo.ax.set_xticklabels(c)
    plt.savefig(out+"_logo.png",dpi=300)




if __name__ == '__main__':

    """
    Script to parse the csv with mutated residue from funclib outputs.
    It takes as input the csv file with the mutated residues.
    """ 

    parser = argparse.ArgumentParser()

    parser.add_argument('-i',
                        '--input',
                        dest='csv',
                        required=True,
                        metavar='',
                        help='csv file from funclib',
                        )

    parser.add_argument('-b',
                        '--barplot',
                        action='store_true',
                        dest='bar',
                        required = False,
                        help='barplot for the rate of mutation along sequence space\
                              or the top 50 pdb'
                        )
    parser.add_argument('-l',
                        '--logo',
                        action='store_true',
                        dest='logo',
                        required = False,
                        help='logo for the rate of mutation along sequence space\
                              or the top 50 pdb'
                        )
    parser.add_argument('-seq',
                        '--sequence_space',
                        action='store_true',
                        dest='seq',
                        required = False,
                        help='perform analysis on the sequence space of the structures\
                              or the entire explored sequence space'
                        )

    parser.add_argument('-t',
                        '--title',
                        type = str,
                        dest='title',
                        required = False,
                        default = '',
                        help='Title name of the barplot'
                        )

    parser.add_argument('-o',
                        '--output_name',
                        type = str,
                        dest='out',
                        required = False,
                        help='Output name'
                        )


    args = parser.parse_args()

    csv = args.csv
    bar = args.bar
    logo = args.logo
    seq = args.seq
    title = args.title
    out = args.out
    if csv.endswith("csv"):
        score = pandas.read_csv(csv)
        score.index.names = [None]
        score.drop('serial_number', axis=1, inplace=True) 
        if seq :
            if logo:
                logos(score,out)
            if bar : 
                barplot(score,title,out)
        else:
            score = score.iloc[1:51]
            if logo:
                logos(score,out)
            if bar : 
                barplot(score,title,out)
    else:
        print("You missed something")
            
        
   


    



                

