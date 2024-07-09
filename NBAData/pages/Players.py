

import streamlit as st
import datetime
import player_info
import team_info
import pandas as pd
from nba_api.stats.endpoints import playercareerstats

st.set_page_config(layout="wide")

#roster_choice = st.radio("Current Or Historical Roster", (["Current Rosters","Historical Rosters"]),horizontal = True, key="roster")


player_select_box = st.selectbox("Choose", player_info.active_players_df["full_name"])
season_choice = ["Regular Season","Career Cumulative", "Playoffs", "Playoffs Cumulative", "All Star Games", "All Star Cumulative", "Regular Season League Ranking", "Playoff League Ranking"]
season_select_box = st.selectbox("Season Type", season_choice)
PerMode = st.radio("Stat Type", ["PerGame","Totals", "Per36"])




player_stats = player_info.choose_player_stats(player_select_box,PerMode,season_select_box)


player_stats_df = pd.DataFrame(player_stats)
#player_sorted_by_year = player_stats_df.sort_values(by="SEASON_ID", ascending = False)

st.header(player_select_box)

player_stats_table = st.dataframe(player_stats_df, hide_index= True, use_container_width=True, column_order= ("SEASON_ID","TEAM_ABBREVIATION","PLAYER_AGE","GP","GS","MIN","PTS","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK","TOV","PF"),column_config= ({"SEASON_ID": "Season","TEAM_ABBREVIATION": "Team","PLAYER_AGE" : "Age","GP":"Games Played","GS" : "Games Started","MIN": 'Minutes Played',"FGM" : 'Field Goals Made',"FGA": "Field Goals Attempted","FG_PCT" :"Field Goal Percentage","FG3M" : "3 Pointers Made","FG3A" : "Field Goals Attempted","FG3_PCT": "3 Point %","FTM" : "Free Throws Made","FTA":"Free Throws Attempted","FT_PCT" :"Free Throw %","OREB": "Offensive Rebounds","DREB": "Defensive Rebounds","REB":"Rebounds","AST": "Assists","STL": "Steals","BLK":"Blocks","TOV" : "Turnover","PF":"Personal Fouls","PTS": "Points"}))









