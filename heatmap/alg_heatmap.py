import pandas as pd
import seaborn as sns; sns.set_theme()

exp = pd.read_table('ptns_hipo_todas.tsv', index_col=0)
ax = sns.heatmap(exp, vmin=0, vmax=31661, cbar=True, xticklabels=True, yticklabels=True)

ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=2)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=2)

figura = ax.get_figure()
figura.savefig('heatmap proteinas hipoteticas NES.png', dpi=400)
