# Python
def number_of_games(df):
    return len(df)

def number_of_games_lfl(df):
    lfl_games = df[df['league'] == 'LFL']
    return len(lfl_games)

def redside_winrate(df):
    red_wins = len(df[df['result'] == 0])
    total_games = len(df)
    return red_wins / total_games

def lfl_teams(df):
    lfl_games = df[df['league'] == 'LFL']
    teams = pd.concat([lfl_games['blue_team'], lfl_games['red_team']])
    return teams.unique()