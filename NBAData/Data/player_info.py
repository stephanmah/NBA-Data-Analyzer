from nba_api.stats.static import players
import pandas as pd


players_list = players.get_players()



playerDF = pd.DataFrame(players_list)




