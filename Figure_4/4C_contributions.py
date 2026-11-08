# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:51:57 2025

@author: asala
"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_4")
print(os.getcwd())

import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

#general aesthetics
sns.set(style='white')

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'
plt.rcParams['font.weight'] = 'bold'

colors = {'smri':"#ee4015",
          'pet': "#a4fa50",
          'fmri':"#ffb00d",
          'uws':"#4d6edf",
          'mcs':"#44ee9a",
          'doc':"#3db9e9",
          }            

#define function

def contribution_charts(df,suffix):

    # Define size of figure
    fig, ax = plt.subplots(figsize=(8, 5))
    ax = sns.histplot(data=df, 
                      y='Contribution_type', hue='Contributor', weights='Percent', 
                      multiple='stack', edgecolor='white',linewidth=0,
                      palette=colors, shrink=0.8
                      )
    ax.invert_yaxis()
    
    
    ax.set_xlim([0,df.Percent.sum(axis=0)/2]) #set lim x axis to N by summing values in N_modality
        
    # Customize the plot
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    #ax.spines['bottom'].set_visible(False)
    
    # # Remove the key
    ax.get_legend().remove()
    
    # # Remove axis labels
    ax.set_xlabel("")
    ax.set_ylabel("")
    
    # # Remove tick labels
    ax.set_yticklabels([])
    
    # # Optionally, remove the ticks themselves
    ax.tick_params(axis='x', colors='#a6a6a6', labelsize=100)
    ax.tick_params(axis='y', which='both', length=0)
    
    # Save the plots with custom names
    outname="studies_contribution_{}.png".format(suffix)
    plt.savefig(outname, dpi=300, bbox_inches='tight', pad_inches=0)
    outname2="studies_contribution_{}.svg".format(suffix)
    plt.savefig(outname2, bbox_inches='tight', pad_inches=0)
    
#we now call the function defined above
df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="contributions")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")
for cluster in df["Cluster"].unique():
    print("Cluster:", cluster)
    #we select the rows (using df.loc) where Cluster==1
    subdf = df.loc[df["Cluster"] == cluster]
    contribution_charts(subdf,cluster)
