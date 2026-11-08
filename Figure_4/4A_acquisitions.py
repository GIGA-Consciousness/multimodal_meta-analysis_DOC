# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:28:34 2025

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

df = pandas.read_excel("Figure_4_input.xlsx", header=0, sheet_name="studies_acquisitions")
df['Variable'] = df['Variable'].astype(str)

rows, columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")

colors = {'fMRI_eyes closed':"#ffb00d",
          'fMRI_eyes open':"#ffb00d",
          'fMRI_not_controlled_for':"#ffb00d",
          'fMRI_NA':"#ffb00d",
          'PET/fMRI_NA':"#DDD645",
          'PET_eyes closed':"#a4fa50",
          'PET_eyes open':"#a4fa50",
          'PET_not_controlled_for':"#a4fa50",
          'PET_NA':"#a4fa50",
          'sMRI/PET_eyes open':"#D7B666",
          'sMRI/PET_NA':"#D7B666",
          'sMRI_NA':"#ee4015",    
         }

#if NA to gray, set dictionary color to "#CBCBCB"

# Define size of figure
fig, ax = plt.subplots(figsize=(20, 0.625)) #adjusted to fit half page!

# #define order to plot the bars
hue_order=list(colors) #assuming list of colors is in the "right" order
hue_order.reverse()

ax = sns.histplot(data=df, 
                  y='Modality_base', hue='Variable', hue_order=hue_order, weights='Frequency', 
                  multiple='stack', edgecolor='white',linewidth=3.5,
                  palette=colors,
                  )

ax.set_xlim(0,35)
# invert xaxis to have bars starting from right y axis
ax.invert_xaxis()

for cont in ax.containers:
    ax.bar_label(cont, label_type='center', fontsize=15, padding=0)
    
#hatch must consist of a string of "*+-./OX\ox|"
hatches=df['info_for_hatches'].tolist() #convert to list 
#hatches.reverse() #to use only if needed
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
plt.savefig("studies_eyes_DOC_HC.png", dpi=300, bbox_inches='tight', pad_inches=0)
plt.savefig("studies_eyes_DOC_HC.svg")
plt.show()