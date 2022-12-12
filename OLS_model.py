from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import IS_415_Project as proj

df = pd.read_csv('teams_col_add.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
df = df.dropna()

r, p = stats.pearsonr(df['elo_diff'], df['point_diff'])
model = np.polyfit(df['elo_diff'], df['point_diff'], 1)

text = 'r - value: ' + str(round(r, 3)) + '\np - value: ' + str(round(p, 3)) 
text += '\nr2 value: '  + str(round(r * r, 3))
text += '\ny = ' + str(round(model[0], 3)) + 'x + ' + str(round(model[1], 3))

sns.set(color_codes = True)
ax = sns.jointplot(x=df['elo_diff'], y=df['point_diff'], kind='reg')

ax.fig.suptitle('elo_diff' + ' and ' + 'point_diff')
ax.fig.tight_layout()
ax.fig.subplots_adjust(top=.95)
ax.fig.text(1, .8, text, fontsize=12, transform=plt.gcf().transFigure)
print(text)
plt.savefig('elo_diff_point_diff.jpg')
plt.show()

