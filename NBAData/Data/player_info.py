62#player_info.py
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd


active_players_data = players.get_active_players()
active_players_df = pd.DataFrame(active_players_data)
active_player_name_to_id = {active_player['full_name']: active_player['id'] for active_player in active_players_data}


#inactive_players_data = players.get_inactive_players()
#inactive_players_df = pd.DataFrame(inactive_players_data)
#inactive_player_name_to_id = {inactive_player['full_name']: inactive_player['id'] for inactive_player in inactive_players_data}


season_stat_type_to_id = {
    "Regular Season" : 0,
    "Career Totals" : 1,
    "Playoffs" : 2,
    "Playoffs Totals" : 3,
    "All Star Games" : 4,
    "All Star Totals": 5,
}




def choose_player_stats(selected_player_id,per_mode, stat_layer):
    player_stats = playercareerstats.PlayerCareerStats(player_id= active_player_name_to_id[selected_player_id],per_mode36=per_mode)
    player_stats_df = player_stats.get_data_frames()[season_stat_type_to_id[stat_layer]]
    return player_stats_df
    
    
    


        