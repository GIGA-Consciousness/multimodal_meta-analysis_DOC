# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:22:32 2025

@author: asala
"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_3")#edit path
print(os.getcwd())

import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

#general aesthetics
sns.set(style='white')

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'
plt.rcParams['font.weight'] = 'bold'

df = pandas.read_excel("Figure_3_input.xlsx", header=0, sheet_name="Measures_included_min5_UWS_MCS")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

#provide colors in the right order
colors = {'PSD': '#46EF98',
'Connectivity': '#38C7DA',
'GT': '#4A9BFA',
'Microstates': '#4958BF',
'Entropy': '#3D3377',
'Complexity': '#37224E',
}                   
          
# Define size of figure
fig, ax = plt.subplots(figsize=(40, 10)) #to be fixed

#define order to plot the bars
hue_order=list(colors) #assuming list of colors is in the "right" order
hue_order.reverse()

ax = sns.histplot(data=df, 
                  y='Band', hue='Subgroup_gen', hue_order=hue_order, weights='N_studies', 
                  multiple='stack', edgecolor='white',linewidth=14,
                  palette=colors,
                  )

ax.set_xlim(0,52)#to be adjusted depending on values

for i, cont in enumerate(ax.containers):
    print(i, cont)
    labels = [f"{v:.0f}" if v > 0 else "" for v in cont.datavalues]  # Conditional, to hide labels when value is 0
    if i in (3,4,5):
       color = "white"
    else:
       color = None
    ax.bar_label(cont, labels=labels, label_type='center', fontsize=60, padding=0, color=color)
  

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
plt.savefig("studies_measures_UWS_MCS.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("studies_measures_UWS_MCS.svg", bbox_inches='tight', pad_inches=0)
plt.show()