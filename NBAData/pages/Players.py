

import streamlit as st
import datetime
import player_info
import team_info

from nba_api.stats.endpoints import playercareerstats


st.set_page_config(layout="wide")

with st.sidebar:
    st.page_link("Home_Page.py", label="Home", icon="🏠")
    st.page_link("pages/Teams.py", label="Team Info")

#roster_choice = st.radio("Current Or Historical Roster", (["Current Rosters","Historical Rosters"]),horizontal = True, key="roster")

PerMode = st.radio("Stat Type", ["Total","PerGame", " Per36"], horizontal= True)


stat_df = playercareerstats.PlayerCareerStats(
    player_id='203897', per_mode36="Totals")
testDF = stat_df.get_data_frames()[11]


player_select_box = st.selectbox("choose", player_info.active_players_df["full_name"])
#stat_selection


#player_stats = player_info.choose_player_stats(player_select_box,stat_type_selector)
with st.container(border=True):
    
    st.write(player_info.active_players_ids_dict[player_select_box])
    
    st.dataframe(testDF)
