# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:59:18 2024

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

df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="foci_by_measure")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'other':"#000000",
'ReHo': "#281F0C",
'instrinc_connectivity_contrast':"#513E18",
'ALFF':"#7F6126",
'functional_connectivity_strength':"#AD8434",
'ICA':"#D3A23F",
'seed-based':"#ffb00d",
'qCMRglc':"#648742",
'SUVr_other':"#92C460",
'SUVr_global':"#a4fa50",
'VBM':"#ee4015"}

# Define size of figure
fig, ax = plt.subplots(figsize=(80, 2.5))

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Measure', weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=14,
                  palette=colors,
                  )

for i, cont in enumerate(ax.containers):
    print(i, cont)
    if i in (8, 9, 10):
       color = "white"
    else:
       color = None
    ax.bar_label(cont, label_type='center', fontsize=60, padding=0, color=color)
    
ax.set_xlim([0,df.Frequency.sum(axis=0)]) #set lim x axis to N by summing values in Frequency

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

# Save the plot
plt.savefig("foci_measures.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("foci_measures.svg")
plt.show()