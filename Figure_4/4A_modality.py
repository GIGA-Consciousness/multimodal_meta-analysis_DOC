# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:59:18 2024

@author: asala
"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_4") #edit path
print(os.getcwd())

import pandas 
import seaborn as sns
import matplotlib.pyplot as plt

#general aesthetics
sns.set(style='white')

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'
plt.rcParams['font.weight'] = 'bold'

df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="studies_by_modality")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'sMRI':"#ee4015",
          'PET': "#a4fa50",
          'fMRI':"#ffb00d",
          'PET/fMRI':'#DDD645',
          'sMRI/PET':'#D7B666'
          }

# Define size of figure
fig, ax = plt.subplots(figsize=(80, 2.5))

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Variable', weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=14,
                  palette=colors,
                  )

for cont in ax.containers:
    ax.bar_label(cont, label_type='center', fontsize=60, padding=0)

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
plt.savefig("studies_modalities.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("studies_modalities.svg")
plt.show()