import pandas as pd
# import help_functions as hf
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import IS_415_Project as proj
import statsmodels

df = pd.read_csv('teams_col_add.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])
df = df.dropna()

print(df.columns)
# print(df.isnull().sum())

home_team_df = df[df['home/away'] == 'Home']
away_team_df = df[df['home/away'] == 'Away']

# All bowl games will be at a neutral site
# We want to predict wins or loses but also the pregame_elo for each team

# df = df.dropna()

# print(df.describe())

# proj.assumptions(df, 'point_diff')