

import streamlit as st
import datetime
import player_info
import team_info


st.set_page_config(layout="wide")

with st.sidebar:
    st.page_link("Home_Page.py", label="Home", icon="🏠")
    st.page_link("pages/Teams.py", label="Team Info")

roster_choice = st.radio("Current Or Historical Roster", (["Current Rosters","Historical Rosters"]),horizontal = True, key="roster")

current_year = datetime.date.today().year
select_year = st.slider("Choose Year", min_value = 1949, max_value = (current_year), value = current_year)

