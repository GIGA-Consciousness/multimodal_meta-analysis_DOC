# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:58:10 2024

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

df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="foci_by_study")

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

fig, ax = plt.subplots(figsize=(14, 14))
plt.margins(x=0)

ax = sns.histplot(data=df, 
                  x='Study_PET', weights='N_PET', 
                  edgecolor='white',linewidth=4,
                  color='#a4fa50',
                  )

ax.set_ylim([0,137])

# Customize the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# # Remove axis labels
ax.set_xlabel("Study", fontsize=80, font='Gill Sans MT', fontweight='bold')
ax.set_ylabel("Foci", fontsize=80, font='Gill Sans MT', fontweight='bold')

# # Remove tick labels
ax.set_xticklabels([])
ax.tick_params(axis='y', labelsize=80)

# # Optionally, remove the ticks themselves
ax.tick_params(axis='x', which='both', length=0)
ax.tick_params(axis='y', which='both', length=0)

# Save the plot
plt.savefig("foci_by_study_PET.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("foci_by_study_PET.svg", bbox_inches='tight', pad_inches=0)
plt.show()