import requests
import pandas as pd
from api_key import api_key

def api_team_stats(team_name):
    url = "https://api.collegefootballdata.com/games"

    payload = ""
    headers = {
    'Authorization': 'Bearer ' + api_key,
    }
    params = {
        'year': 2022,
        'team': team_name,
        'seasonType': 'regular'
    }

    response = requests.request("GET", url, headers=headers, data=payload, params=params)

    response = response.json()

    return(response)

bowl_team_names = [
    'Miami (OH)', 'UAB', 'UT San Antonio', 'Troy', 
    'Cincinnati', 'Louisville', 'Jackson State', 
    'North Carolina Central', 'Florida', 'Oregon State', 
    'Washington State', 'Fresno State', 'Rice', 
    'Southern Mississippi', 'SMU', 'BYU', 'North Texas',
    'Boise State', 'Marshall','Connecticut',
    'Eastern Michigan', 'San José State', 'Liberty',
    'Toledo', 'Western Kentucky', 'South Alabama',
    'Baylor', 'Air Force', 'Louisiana', 'Houston',
    'Wake Forest', 'Missouri', 'Middle Tennessee',
    'San Diego State', 'New Mexico State', 'Bowling Green',
    'Georgia Southern', 'Buffalo', 'Memphis', 'Utah State',
    'Coastal Carolina', 'East Carolina', 'Wisconsin',
    'Oklahoma State', 'UCF', 'Duke', 'Kansas',
    'Arkansas', 'North Carolina', 'Oregon',
    'Texas Tech', 'Ole Miss', 'Syracuse', 'Minnesota',
    'Oklahoma', 'Florida State', 'Texas', 'Washington',
    'Maryland', 'NC State', 'Pittsburgh', 'UCLA',
    'Notre Dame', 'South Carolina', 'Ohio',
    'Wyoming', 'Tennessee', 'Clemson',
    'Alabama', 'Kansas State', 'Iowa', 'Kentucky',
    'TCU', 'Michigan', 'Ohio State', 'Georgia',
    'Mississippi State', 'Illinois', 'Tulane',
    'USC', 'LSU', 'Purdue', 'Penn State', 'Utah'
]

col_names = ['team_name', 'week', 'neutral_site', 'conference_game', 
'home_team', 'home_points', 'home_post_win_prob', 'home_pregame_elo', 'home_postgame_elo',
'away_team', 'away_points', 'away_post_win_prob', 'away_pregame_elo', 'away_postgame_elo',
]

teams_df = pd.DataFrame(columns=col_names)

for team in bowl_team_names:
    stats = api_team_stats(team)
    for game in stats:
        team_name = team
        week = game['week']
        neutral_site = game['neutral_site']
        conference_game = game['conference_game']
        home_team = game['home_team']
        home_points = game['home_points']
        home_post_win_prob = game['home_post_win_prob']
        home_pregame_elo = game['home_pregame_elo']
        home_postgame_elo = game['home_postgame_elo']
        away_team = game['away_team']
        away_points = game['away_points']
        away_post_win_prob = game['away_post_win_prob']
        away_pregame_elo = game['away_pregame_elo']
        away_postgame_elo = game['away_postgame_elo']

        teams_df = teams_df.append({'team_name':team_name, 'week':week, 'neutral_site': neutral_site, 'conference_game': conference_game, 
        'home_team':home_team, 'home_points':home_points, 'home_post_win_prob':home_post_win_prob, 
        'home_pregame_elo':home_pregame_elo, 'home_postgame_elo':home_postgame_elo, 
        'away_team':away_team, 'away_points':away_points, 'away_post_win_prob':away_post_win_prob, 
        'away_pregame_elo':away_pregame_elo, 'away_postgame_elo':away_postgame_elo}, ignore_index=True)

teams_df.to_csv('teams_df.csv', index=True)