from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd


active_players_list = players.get_active_players()
active_players_df = pd.DataFrame(active_players_list)
active_players_ids_dict = {active_player['full_name']: active_player['id'] for active_player in active_players_list}


inactive_players_list = players.get_inactive_players()
inactive_players_df = pd.DataFrame(inactive_players_list)
inactive_players_ids_dict = {inactive_player['full_name']: inactive_player['id'] for inactive_player in inactive_players_list}


season_stat_type_dict = {
    "Regular Season" : 0,
    "Career Cumulative" : 1,
    "Playoffs" : 2,
    "Playoffs Cumulative" : 3,
    "All Star Games" : 4,
    "All Star Cumulative": 5,
    "Regular Season League Rank" : 10,
    "Playoff Stat League Rank" : 11
}


#def get_player_stats():

"""
playercareerstats layers
0 career season stats *
1 career cumulative
2 playoffs  stats 
3playoff cumulative* 
4all star game stats
5 asg totals
6 college stats?
7 college cum?
8?
9 ?
10 reg season league rank
11 play off league rank


"""

#def choose_rank():
