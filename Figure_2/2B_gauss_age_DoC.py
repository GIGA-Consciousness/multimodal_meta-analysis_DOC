# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:09:36 2024

@author: thoth
"""

import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_2") #edit path
print(os.getcwd())

import pandas
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm

#set font to Gill Sans MT
plt.rcParams['font.family'] = 'Gill Sans MT'

colors = {"EEG": "#3DB9E9",
          "MRI": "#F78137",
          "PET": "#A4FA50",
          "fNIRS": "#E30052"}


df = pandas.read_excel("Figure_2_input.xlsx", header=0, sheet_name="age_DoC")

#low = (df["mean"] - 3 * df["sigma"]).min()
#high = (df["mean"] + 3 * df["sigma"]).max()

low = 5     #min DOC
high = 92   #max DOC
#low = 5     #min HC
#high= 85    #max HC

x = np.linspace(low, high, 1000)

dist = np.zeros_like(x)

plt.figure(figsize=(20,14))
  
  
for i, row in df.iterrows():
    #range = [row["mean"] - 2 * row["sigma"],
    #         row["mean"] + 2 * row["sigma"]]
    #range = [low, high] #for fixed min max range
    range = [row["min"],row["max"]]
    cdf = norm.cdf(range, row["mean"], row["sigma"])
    scale = row["N"] / (cdf[1] - cdf[0])
    #scale = row["N"]
    pdf = scale * norm.pdf(x, row["mean"], row["sigma"])
    pdf[(x < range[0]) | (x > range[1])] = 0 #add if truncate gaussians at study-specific min-max
    dist += pdf
  
    plt.plot(x, 25*pdf, color=colors.get(row["modality"], "k"),
             linestyle="--",
             linewidth=4)
    

#take average of summed pdf
#dist = dist / len(df) #average not not used

#plt.plot(x, dist, "g", linewidth=10) #HC version
plt.plot(x, dist, "k", linewidth=10) 
plt.xlabel ('Age (years)', fontsize=60, labelpad=30)
#plt.ylabel ('Total observations')
plt.ylabel ('Observations per study', fontsize=60, labelpad=30)
plt.ylim(bottom=0)
ax = plt.gca()
ax.set_xlim([0, 92])
ax.tick_params(axis='x', labelsize=60)
ax.set_ylim([0, 140]) #changed to 140 (from 100)
ax.tick_params(axis='y', labelsize=60)
# plt.annotate("N=40", xy=(50, 5))
#plt.fill_between(x,dist, color='darkseagreen') #HC version
plt.fill_between(x,dist, color='#386273') #DoC version
ax.yaxis.tick_right() #DoC version
ax.yaxis.set_label_position("right")  #DoC version
plt.yticks([0,25,50,75,100,125],[0,1,2,3,4,5]) #to be revised if ylim changed from different than 0-100 and pdf multiplied by other than 20
plt.tight_layout()

# Customize the spines (the lines around the chart)
for spine in plt.gca().spines.values():  # Loop through all spines
    spine.set_linewidth(3)  # Set spine width (default is usually 1)
    
# Make right axis dashed
ax = plt.gca()  # Get current axes
ax.spines['right'].set_linestyle((0, (6, 6)))  # Dashed line (pattern: 5 on, 5 off)


# Save the plot with 300 DPI
plt.savefig("DOC_plot_300dpi_truncated.png", dpi=300)
plt.savefig('DOC_plot_300dpi_truncated.svg')
#plt.savefig("DoC_plot_nogrid_300dpi.png", dpi=300)

plt.show()

#get descriptive stats
mean= np.average(x, weights = dist)

dev=dist * (x - mean) ** 2
dev_std=np.sqrt(dev.sum() / (dist.sum() - 1))

print(mean)
print(dev_std)

