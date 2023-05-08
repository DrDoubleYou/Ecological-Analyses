import csv
import numpy as np
import matplotlib.pyplot as plt

with open("species_richness.csv","r") as s:
    soils = list(csv.reader(s))
    soils[0][0]="OF"

areas=[[],[],[],[]]

for row in soils[1:]:
    for area in range(len(row)):
        areas[area].append(float((row[area])))

of = np.array(areas[0])
mt = np.array(areas[1])
lt = np.array(areas[2])
cc = np.array(areas[3])

of_mean = np.mean(of)
mt_mean = np.mean(mt)
lt_mean = np.mean(lt)
cc_mean = np.mean(cc)

of_std = np.std(of)
mt_std = np.std(mt)
lt_std = np.std(lt)
cc_std = np.std(cc)

stages = soils[0]
x_pos  = np.arange(len(stages))
means  = [of_mean, mt_mean, lt_mean, cc_mean]
error  = [of_std, mt_std, lt_std,cc_std]

plt.rcParams["font.family"] = "Times New Roman"

fig, ax = plt.subplots()
ax.bar(x_pos, means, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Mean Species Richness')
ax.set_xticks(x_pos)
ax.set_xticklabels(stages)
ax.set_title('Stage vs Mean Species Richness')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# Save the figure and show
plt.savefig('mean_species_richness_bar_graph.png')
plt.show()

