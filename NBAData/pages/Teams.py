import streamlit as st

import datetime
import team_info
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.page_link("Home_Page.py", label="Home", icon="🏠")
    st.page_link("pages/Players.py", label="Players Info")

st.title("Team Stats")


season_type_selector = st.radio(
    "Season Type", (["Regular Season", "Pre Season"]), horizontal=True, key="roster")
current_year = datetime.date.today().year


nba_teams_selectbox = st.selectbox(
    "NBA Teams", team_info.team_list_DF["full_name"], placeholder="Choose A Team", disabled=False, index=0)


with st.container(border=True):
    # col1, col2, col3 = st.columns(3)

    st.image(team_info.nba_logo_dict[nba_teams_selectbox])
    st.header("Team Standings")
    st.subheader(nba_teams_selectbox)

    first_year = 1949
    years_array = []
    
    for years in range(first_year,current_year)[::-1]:
        years_array.append(years)


    #select_year_slider = st.slider("Choose Year", min_value=1949,max_value=(current_year), value=current_year)
    select_year = st.selectbox("Choose year", options=(years_array))


    basic_team_stats = team_info.choose_basic_stats(nba_teams_selectbox, select_year, season_type_selector)
    basic_team_stats_df = pd.DataFrame(basic_team_stats.get_data_frames()[0])

    basic_stats_teams_table = st.dataframe(basic_team_stats_df, hide_index=True, use_container_width=True,column_order=( "SEASON_YEAR", "TEAM_CONFERENCE", "TEAM_DIVISION", "W",   "L",    "PCT",  "MIN_YEAR"),
    column_config=({"SEASON_YEAR": "Season", "TEAM_CONFERENCE": "Conference", "TEAM_DIVISION": "Division",
    "W": "Wins",   "L": "Losses",    "PCT": "Win %", "MIN_YEAR": "First Season"}))

with st.container(border=True):
    st.header("Advanced Team Stats")
    per_mode = st.radio("Per Mode", (["PerGame", "Totals"]))

    advanced_team_stats = team_info.choose_advanced_stats( nba_teams_selectbox, per_mode, season_type_selector)

    advanced_team_stats_df = pd.DataFrame(advanced_team_stats.get_data_frames()[0])

    team_sorted_by_year = advanced_team_stats_df.sort_values(by='YEAR', ascending=False)

    advanced_team_stats_table = st.dataframe(
        team_sorted_by_year, hide_index=True, use_container_width=True, column_order=("TEAM_NAME", "YEAR",  "GP",  "WINS",  "LOSSES",  "WIN_PCT",  "CONF_RANK",  "DIV_RANK",  "PO_WINS",  "PO_LOSSES",  "NBA_FINALS_APPEARANCE",   "FGM",   "FGA",  "FG_PCT",  "FG3M",  "FG3A",  "FG3_PCT",   "FTM",   "FTA",  "FT_PCT",  "OREB",  "DREB",   "REB",   "AST",    "PF",  "STL",   "TOV",  "BLK",    "PTS",  "PTS_RANK"
                                                                                 ), column_config=({"TEAM_CITY": "Team City", "TEAM_NAME": "Team Name",     "YEAR": "Season",  "GP": "Games Played",  "WINS": "Wins",  "LOSSES": "Losses",  "WIN_PCT": "Win %",  "CONF_RANK": "Conference Rank",  "DIV_RANK": "Division Rank",  "PO_WINS": "Playoff Wins",
                                                                                                    "PO_LOSSES": "Playoff Losses",  "CONF_COUNT": "Conference Count",  "DIV_COUNT": "Division Count", "NBA_FINALS_APPEARANCE": "Finals Appearance",   "FGM": "Field Goals Made",   "FGA": "Field Goals Attempted",  "FG_PCT": "Field Goals Attempted",  "FG3M": "3 Pointers Made",  "FG3A": "3 Pointers Attempted",  "FG3_PCT": "3 Point %",   "FTM": "Free Throws Made",   "FTA": "Free Throws Attempted",  "FT_PCT": "Free Throw %",  "OREB": "Offensive Rebounds",  "DREB": "Defensive Rebounds",   "REB": "Rebounds",   "AST": "Assists",    "PF": "Personal Fouls",  "STL": "Steals",   "TOV": "Turnovers",  "BLK": "Blocks",    "PTS": "Points",  "PTS_RANK": "Points Ranking"
                                                                                                    }))


# basic_team_stats_df
