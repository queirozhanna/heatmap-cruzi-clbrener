import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

exp = pd.read_table('DEGs_metab_energ.tsv', index_col=0)
ax = sns.heatmap(exp, vmin=0, vmax=22273, cmap=sns.diverging_palette(100, 5, center="dark", as_cmap=True), cbar=True, xticklabels=True, yticklabels=True)

ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=5)

figura = ax.get_figure()
figura.savefig('heatmap DEGs metabolismo energético.png', dpi=400)
