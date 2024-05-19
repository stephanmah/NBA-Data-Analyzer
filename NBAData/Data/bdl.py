import sqlite3
import pandas as pd
import sys
sys.path.insert(1, 'Data')
sys.path.insert(1, 'NBAData/pages')
import team_info
import Teams
con = sqlite3.connect("teams.db")
cur = con.cursor()
#cur.execute("CREATE TABLE teams(TEAM_ID,SEASON_YEAR,TEAM_CITY,TEAM_NAME,TEAM_ABBREVIATION,TEAM_CONFERENCE, TEAM_DIVISION, TEAM_CODE, TEAM_SLUG,   W,   L,    PCT,  CONF_RANK,  DIV_RANK, MIN_YEAR, MAX_YEAR)")
print(Teams.basic_team_stats_df)

res = cur.execute("SELECT * FROM teams")
res.fetchall()

