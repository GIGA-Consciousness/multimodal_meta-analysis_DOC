
import pandas
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm
import matplotlib.ticker as ticker
from matplotlib import font_manager


import os
os.chdir(r"C:\Users\asala\Dropbox\Meta-analysis\paper\figures\Figure_2") #edit path

# Font
font_path = "GIL_____.TTF"
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)
font_family_name = prop.get_name()
plt.rcParams['font.family'] = font_family_name

# Colors
colors = {"EEG": "#3DB9E9",
          "MRI": "#F78137",
          "PET": "#A4FA50",
          "fNIRS": "#E30052"}

# DOC min/max
low = 0     #min DOC
high = 423.484467414282   #max DOC

# Plot Size, in inches
width = 32
heght = 14

# Plot resolution, dpi
dpi = 300

# Cummulative axis limit
cumm_max = 360

# Individual axis limit
indiv_max = 75

# Do not print points lower than that value (set to 0 to deactivate)
crop = 0

# Font and label sizes
fontsize = 60

# Basic linewidth
lw_normal = 4

# Fat linewidth
lw_fat = 10

# Alpha for individual lines
alpha = 0.8

# Output name (without extension)
out = "DoC_plot_nogrid_300dpi"
############################################################################

df = pandas.read_excel("Figure_2_input.xlsx", header=0, sheet_name="tsi")

x = np.linspace(low, high, 10000)
dist = np.zeros_like(x)

fig, ax1 = plt.subplots(figsize=(width, heght))


ax1.set_ylim([0, cumm_max])
for spine in ax1.spines.values():
    # Setting axes width to 4
    spine.set_linewidth(lw_normal)
# Dashed line (pattern: 5 on, 5 off)
ax1.spines['right'].set_linestyle((0, (4, 4)))
ax1.set_xlabel('Time since injury (months)', fontsize=fontsize, labelpad=fontsize/2)
ax1.set_ylabel ('Cumulative observations across studies', fontsize=fontsize, labelpad=fontsize/2)
#ax1.yaxis.set_label_coords(-0.065,0.43)
ax1.yaxis.set_label_coords(-0.065,0.40)
ax1.tick_params(axis='x', labelsize=fontsize, width=3, length=15)
ax1.tick_params(axis='x', which="minor", width=2, length=10)
ax1.tick_params(axis='y', labelsize=fontsize)
ax1.set_xscale("log") #transform to log
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:g}'.format(y)))

ax2 = ax1.twinx()
ax2.set_ylim([0, indiv_max])
for spine in ax2.spines.values():
    # Disabeling spines
    spine.set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['left'].set_linewidth(lw_fat)
ax2.spines['left'].set_zorder(len(df) + 10)
ax2.set_ylabel('Observations per study',
               fontsize=fontsize, labelpad=fontsize/2,
               color='black')
ax2.tick_params(axis='y', labelsize=fontsize)

# Plotting the distributions
for i, row in df.iterrows():
    range = [row["min"],row["max"]]
    cdf = norm.cdf(range, row["mean"], row["sigma"]) #integral of a normal distribution with given parameters
    scale = row["N"] / (cdf[1] - cdf[0])
    pdf = scale * norm.pdf(x, row["mean"], row["sigma"])
    pdf[(x < range[0]) | (x > range[1])] = 0 #add if truncate gaussians at study-specific min-max
    dist += pdf
  
    crop_x = x[pdf >= crop]
    pdf = pdf[pdf >= crop]
    ax2.plot(crop_x, pdf, color=colors.get(row["modality"], "k"),
             linestyle="--",
             alpha=alpha,
             linewidth=lw_normal,
             zorder=float(i))

crop_x = x[dist >= crop]
crop_dist = dist[dist >= crop]
ax1.fill_between(crop_x, crop_dist, color='#386273', zorder=float(len(df)))
ax1.plot(crop_x, dist, "k", linewidth=lw_fat, zorder=float(len(df) + 1))


fig.tight_layout()
plt.savefig(out + ".png", dpi=dpi)
plt.savefig('tsi_plot.svg')

# Printing stats
mean = np.average(x, weights=dist)

dev = dist * (x - mean) ** 2
dev_std = np.sqrt(dev.sum() / (dist.sum() - 1))

print("Mean: {};\nSTD: {}".format(mean, dev_std))
with open(out + ".tsv", "w") as f:
    f.write("{}\t{}\n".format("x", "y"))
    for x, y in zip(x, dist):
        f.write("{:0.4f}\t{:0.4f}\n".format(x, y))

