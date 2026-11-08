# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 18:55:55 2025

@author: asala
"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_2") #edit path
print(os.getcwd())

import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

#general aesthetics
sns.set(style='white')

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'
plt.rcParams['font.weight'] = 'bold'

df = pandas.read_excel("Figure_2_input.xlsx", header=0, sheet_name="etiology")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'TBI':"#4D6EDF",
          'NTBI': "#5E9CB4",
          'Anoxia':"#9EDCF7",
          'Others':'#CBCBCB'
          }

# Define size of figure
fig, ax = plt.subplots(figsize=(28.88, 3)) #length to be adjusted to proportion of DoC, HC 1372 DOC 3562, tot 4.934 -> 28.88

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Variable', weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=8,
                  palette=colors, #alpha=1 #this parameter controls transparency of colors
                  hatch='/'
                  )

for cont in ax.containers:
    ax.bar_label(cont, label_type='center', fontsize=60, padding=0)

ax.set_xlim([0,df.N_modality.sum(axis=0)]) #set lim x axis to N by summing values in N_modality


# Customize the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# # Remove the key
ax.get_legend().remove()

# # Remove axis labels
ax.set_xlabel("")
ax.set_ylabel("")

# # Remove tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# # Optionally, remove the ticks themselves
ax.tick_params(axis='x', which='both', length=0)
ax.tick_params(axis='y', which='both', length=0)

#plot in the right order
ax.invert_xaxis()

# Customize the plot
plt.savefig("observations_etiology.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig('observation_etiology_plot.svg')
plt.show()