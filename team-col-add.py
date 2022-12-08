import pandas as pd

teams_stats_df = pd.read_csv('teams_df.csv')

# print(teams_stats_df.head())

for row in teams_stats_df.itertuples():

    if row.team_name == row.home_team:
        point_diff = row.home_points - row.away_points
        elo_diff = row.home_pregame_elo - row.home_postgame_elo

        teams_stats_df.at[row.Index, 'elo_diff'] = elo_diff
        teams_stats_df.at[row.Index, 'point_diff'] = point_diff
        teams_stats_df.at[row.Index, 'home/away'] = 'Home'

        if point_diff > 0:
            teams_stats_df.at[row.Index, 'win/loss'] = 'W'
        else:
            teams_stats_df.at[row.Index, 'win/loss'] = 'L'

    elif row.team_name == row.away_team:
        point_diff = row.away_points - row.home_points
        elo_diff = row.away_pregame_elo - row.away_postgame_elo

        teams_stats_df.at[row.Index, 'elo_diff'] = elo_diff
        teams_stats_df.at[row.Index, 'point_diff'] = point_diff
        teams_stats_df.at[row.Index, 'home/away'] = 'Away'

        if point_diff > 0:
            teams_stats_df.at[row.Index, 'win/loss'] = 'W'
        else:
            teams_stats_df.at[row.Index, 'win/loss'] = 'L'

teams_stats_df.to_csv('teams_col_add.csv', index=True)

        
