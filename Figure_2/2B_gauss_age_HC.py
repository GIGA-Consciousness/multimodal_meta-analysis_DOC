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


df = pandas.read_excel("Figure_2_input.xlsx", header=0, sheet_name="age_HC")

#fixed min max range
low = 5.8     #min HC
high= 80    #max HC

x = np.linspace(low, high, 1000)

dist = np.zeros_like(x)
plt.figure(figsize=(20,14))
  
  
for i, row in df.iterrows():
    range = [row["min"],row["max"]]
    cdf = norm.cdf(range, row["mean"], row["sigma"])
    scale = row["N"] / (cdf[1] - cdf[0])
    #scale = row["N"]
    pdf = scale * norm.pdf(x, row["mean"], row["sigma"])
    pdf[(x < range[0]) | (x > range[1])] = 0 #truncating gaussians at study-specific min-max
    dist += pdf
  
    
    plt.plot(x, 25*pdf, color=colors.get(row["modality"], "k"),
             linestyle="--",
             linewidth=4)
    
plt.plot(x, dist, "k", linewidth=10)
plt.xlabel ('Age (years)', fontsize=60, labelpad=30)
plt.ylabel ('Cumulative observations across studies', fontsize=60, labelpad=30)
plt.ylim(bottom=0)
ax = plt.gca()
ax.set_xlim([0, 92])
ax.tick_params(axis='x', labelsize=60)
ax.set_ylim([0, 140])
ax.tick_params(axis='y', labelsize=60)
ax.yaxis.set_label_coords(-0.065,0.43) #move y label to fit space better
# plt.annotate("N=40", xy=(50, 5))
plt.fill_between(x,dist, color='#58733e')  
#ax.yaxis.set_label_position("right") #DoC version
plt.yticks([20,40,60,80,100,120],[20,40,60,80,100,120]) #to be revised if ylim changed
plt.tight_layout()

# Customize the spines (the lines around the chart)
for spine in plt.gca().spines.values():  # Loop through all spines
    spine.set_linewidth(3)  # Set spine width (default is usually 1)

ax.spines['left'].set_linewidth(10)

# Save the plot with 300 DPI
plt.savefig("HC_plot_300dpi_truncated.png", dpi=300)
plt.savefig('HC_plot_300dpi_truncated.svg')

plt.show()

#get descriptive stats
mean= np.average(x, weights = dist)

dev=dist * (x - mean) ** 2
dev_std=np.sqrt(dev.sum() / (dist.sum() - 1))

print(mean)
print(dev_std)





