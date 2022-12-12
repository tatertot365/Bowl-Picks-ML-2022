from OLS_model import model
from decision_tree_pred import predictions_decision_tree
import pandas as pd
import numpy as np

predict = np.poly1d(model)
point_diff_array = predict([
    (1382-1513), 
    (1679-1564),
    (1739-1704),
    (0-0),
    (1650-1724),
    (1644-1709),
    (1073-1289),
    (1506-1524),
    (1453-1717),
    (1576-1128),
    (1364-1480),
    (1414-1494),
    (1663-1515),
    (1709-1731),
    (1569-1606),
    (1663-1470),
    (1369-1487),
    (1236-1123),
    (1381-1389),
    (1513-1398),
    (1443-1445),
    (1710-1541),
    (1647-1466),
    (1366-1693),
    (1599-1729),
    (1591-1676),
    (1462-1760),
    (1660-1850),
    (1931-1729),
    (1646-1585),
    (1688-1683),
    (1858-1612),
    (1495-1359),
    (1977-1821),
    (2151-1892),
    (1709-1645),
    (1855-2144),
    (2108-2132),
    (1675-1768),
    (1675-1785),
    (1729-1622),
    (1979-1896)
])

win_loss_array = []

for points in point_diff_array:
    if points > 0:
        win_loss_array.append('W')
        print(f'Home team wins by {points} points')
    else:
        win_loss_array.append('L')
        print(f'Home team loses by {abs(points)} points')

teams_df = pd.read_csv('teams_df.csv')
game_array = []
unique_teams = teams_df['team_name'].unique()

for i in range(0, len(unique_teams), 2):
    game_array.append(unique_teams[i] + ' vs ' + unique_teams[i+1])

pred_df = pd.DataFrame(data={'Games':game_array, 'Predicted Winnter OLS':win_loss_array, 'predictions_decision_tree':predictions_decision_tree})
pred_df.to_csv('predictions.csv', index=False)