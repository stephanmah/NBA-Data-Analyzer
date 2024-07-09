import streamlit as st
import sys

sys.path.insert(1, 'Data')
st.set_page_config(layout="wide")
sys.path.insert(1, './NBAData/Data/')
import team_info

st.title("NBA Data Analyzer")

#st.write(team_info.teamDF)
