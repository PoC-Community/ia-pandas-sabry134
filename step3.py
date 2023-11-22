# Python
def aphelios_vs_ezreal(df):
    aphelios_ezreal_games = df[((df['blueadc'] == 'Aphelios') & (df['redadc'] == 'Ezreal')) | 
                                ((df['blueadc'] == 'Ezreal') & (df['redadc'] == 'Aphelios'))]
    
    aphelios_wins = len(aphelios_ezreal_games[((aphelios_ezreal_games['blueadc'] == 'Aphelios') & 
                                               (aphelios_ezreal_games['result'] == 1)) | 
                                              ((aphelios_ezreal_games['redadc'] == 'Aphelios') & 
                                               (aphelios_ezreal_games['result'] == 0))])
    
    winrate = aphelios_wins / len(aphelios_ezreal_games)
    
    return winrate