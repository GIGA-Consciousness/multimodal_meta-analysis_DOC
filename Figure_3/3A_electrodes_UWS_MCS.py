# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:10:37 2025

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

df = pandas.read_excel("Figure_3_input.xlsx", header=0, sheet_name="Electrodes_UWS_MCS")
df['Variable'] = df['Variable'].astype(str)

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'8':'#3DB9E9',  
          '12':'#3DB9E9',
          '16':'#3DB9E9',
          '19':'#3DB9E9',
          '32':'#3DB9E9',
          '64':'#3DB9E9',
          '128':'#3DB9E9',
          '256':'#3DB9E9'
 }

# Define size of figure
fig, ax = plt.subplots(figsize=(10, 0.41)) 
#Decrease size to increase visibility of hatches

# #define order to plot the bars
hue_order=list(colors) #assuming list of colors is in the "right" order
hue_order.reverse()

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Variable', hue_order=hue_order, weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=3.5,
                  palette=colors,
                  )

ax.set_xlim(0,52)#to be adjusted depending on values;

for cont in ax.containers:
    ax.bar_label(cont, label_type='center', fontsize=15, padding=0)
    
#hatch must consist of a string of "*+-./OX\ox|"
hatches=df['info_for_hatches'].tolist() #convert to list 
for hues, hatch in zip(ax.containers, hatches):
    # set a different hatch for each time
    for hue in hues:
        hue.set_hatch(hatch)


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
plt.savefig("studies_electrodes_UWS_MCS.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("studies_electrodes_UWS_MCS.svg", bbox_inches='tight', pad_inches=0)
plt.show()