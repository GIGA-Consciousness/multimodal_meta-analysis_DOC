# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:10:37 2025

@author: asala

"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_4")#edit path
print(os.getcwd())

import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

#general aesthetics
sns.set(style='white')

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'
plt.rcParams['font.weight'] = 'bold'

df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="studies_sedation")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'fMRI_Exclusion criteria':"#ffb00d",
          'fMRI_Sedation possible':"#ffb00d",
          'fMRI_NA':"#ffb00d",
          'PET/fMRI_Exclusion criteria':"#DDD645",
          'PET/fMRI_Sedation possible':"#DDD645",
          'PET_Exclusion criteria':"#a4fa50",
          'PET_Sedation possible':"#a4fa50",
          'PET_NA':"#a4fa50",
          'sMRI/PET_Exclusion criteria':"#D7B666",
          'sMRI/PET_NA':"#D7B666",
          'sMRI_NA':"#ee4015"        
          }

# Define size of figure
fig, ax = plt.subplots(figsize=(20, 0.625))

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Variable', weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=3.5,
                  palette=colors,
                  )

for cont in ax.containers:
    ax.bar_label(cont, label_type='center', fontsize=15, padding=0)
    
#hatch must consist of a string of "*+-./OX\ox|"
hatches=df['info_for_hatches'].tolist() #convert to list 
hatches.reverse() #to align with order in with plot is stored
for hues, hatch in zip(ax.containers, hatches):
    # set a different hatch for each time
    for hue in hues:
        hue.set_hatch(hatch)

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
plt.savefig("studies_sedation.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("studies_sedation.svg")
plt.show()