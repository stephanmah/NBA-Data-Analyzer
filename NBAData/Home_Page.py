import streamlit as st
import sys

sys.path.insert(1, 'Data')
st.set_page_config(layout="wide")
#sys.path.insert(1, './NBAData/Data/')
import team_info

st.title("NBA Data Analyzer")

#st.write(team_info.teamDF)

with st.sidebar:
    st.page_link("Home_Page.py", label= "Home", icon = "🏠")
    st.page_link("pages/Teams.py", label = "Team Info")
    st.page_link("pages/Players.py", label="Players Info")
