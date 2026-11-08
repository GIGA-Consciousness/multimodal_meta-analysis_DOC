import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

labels = ["fNIRS","EEG", "EEG_PET", "PET", "PET_MRI", "MRI", "EEG_PET_MRI"]
sizes = [2, 76, 1, 15, 3, 24, 2]
colors = ["#E30052", "#3DB9E9", "#44EE9A", "#A4FA50", "#EBCE4C", "#F78137", "#ABB29C"]

total = 0
for x in sizes:
    total += x
total = math.sqrt(total)
scale = math.sqrt(sizes[-1]) / total
print(total, scale)
explode = [0.03] * (len(sizes) - 1)
fig, ax = plt.subplots()

ax.pie(sizes[:-1], shadow=False, colors=colors[:-1],wedgeprops=dict(edgecolor='w'))

c = Circle((0, 0), radius=scale, facecolor=colors[-1], edgecolor='w')
ax.add_patch(c)

plt.savefig('pie_plot.svg')

plt.show()