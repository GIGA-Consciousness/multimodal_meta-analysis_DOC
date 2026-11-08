#create environment based on requirements.txt
import matplotlib.pyplot as plt
import pandas

from matplotlib import font_manager
font_path = "GIL_____.TTF"
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)
font_family_name = prop.get_name()
plt.rcParams['font.family'] = font_family_name
plt.rcParams['font.weight'] = "normal"
plt.rcParams['font.size'] = 16.4

patterns = {"circle": "|",
            "pch": ".",
            "": ""}

table = "Figure_4_input.xlsx" #edit filename
sheet = "surfaces"
out = "{}_{}.tiff".format(table.rsplit(".")[0], sheet)

df = pandas.read_excel(table, sheet_name=sheet)

fig, ax = plt.subplots()
fig.set_size_inches(7.25, 13.3)
fig.subplots_adjust(left=0.35, bottom=0.049, right=0.99, top=0.996)

ax.set_xlim(-0.235, 0.535)
ax.set_ylim(0.630, 15.9)

ax.set_xlabel("Correlation Coefficient", size=20.6, labelpad=2)

ax.spines[['right', 'top']].set_visible(False)

pos_labels = df["Position_label"].dropna()
labels = [l.strip().replace("α", "@").replace("β", "@")
          for l in df.loc[pos_labels.index, "Map_label_extended"]
          ]
ax.set_yticks(pos_labels, labels)
[t.set_alpha(0.7) for t in ax.yaxis.get_ticklabels()]
[t.set_alpha(0.8) for t in ax.xaxis.get_ticklabels()]

ax.tick_params(which='major', width=1.00, length=3, pad=2)
x_ticks = (-0.2, 0, 0.2, 0.4)
x_labels = ["{}".format(x).replace("-", "-")
            for x in x_ticks]
ax.set_xticks(x_ticks, x_labels)

for x in x_ticks:
    ax.plot([x, x], ax.get_ylim(), linestyle="--",
            dashes=(5, 4),
            color="black", alpha=1.0, linewidth=0.5, zorder=0)


if "Pattern_type" in df.columns:
    df["Pattern_type"] = df["Pattern_type"].fillna("").replace(patterns)
    hatch = df["Pattern_type"]
else:
    hatch = None

ax.barh(df["Position"], df["R"],
        color=df["Color_basic"],
        edgecolor=df["Color_basic_border"],
        hatch=hatch,
        hatchcolor="white",
        lw=1, height=0.45)

for _, row in df.iterrows():
    ax.plot([row["R"], 0.5], [row["Position"], row["Position"]],
            linestyle="dotted", color="gray", alpha=0.4) 

#plt.subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.1)
ax.vlines(x=[0], ymin=ax.get_ylim()[0], ymax=ax.get_ylim()[1],
          colors="red", linewidth=2)

plt.savefig(out, dpi=700, pil_kwargs={"compression": "tiff_lzw"})
