#team_info.py
from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamInfoCommon, TeamYearByYearStats
import pandas as pd
from random import randrange
import time

teams_list = teams.get_teams()

team_list_DF = pd.DataFrame(teams_list)






nba_colors_dict = {"Atlanta Hawks": "#e03a3e",
                   "Boston Celtics": "#007a33",
                   "Brooklyn Nets": "#000000",
                   "Charlotte Hornets": "#1d1160",
                   "Chicago Bulls": "#ce1141",
                   "Cleveland Cavaliers": "#860038",
                   "Dallas Mavericks": "#00538c",
                   "Denver Nuggets": "#0e2240",
                   "Detroit Pistons": "#c8102e",
                  " Golden State Warriors": "#1d428a",
                   "Houston Rockets": "#ce1141",
                   "Indiana Pacers": "#002d62",
                   "Los Angeles Clippers": "#c8102e",
                   "Los Angeles Lakers": "#552583",
                   "Memphis Grizzlies": "#5d76a9",
                   "Miami Heat": "#98002e",
                   "Milwaukee Bucks": "#00471b",
                   "Minnesota Timberwolves": "#0c2340",
                   "New Orleans Pelicans": "#0c2340",
                   "New York Knicks": "#006bb6",
                   "Oklahoma City Thunder": "#007ac1",
                   "Orlando Magic": "#0077c0",
                   "Philadelphia 76ers": "#006bb6",
                   "Phoenix Suns": "#1d1160",
                  "Portland Trail Blazers": "#e03a3e",
                   "Sacramento Kings": "#5a2d81",
                   "San Antonio Spurs": "#c4ced4",
                   "Toronto Raptors": "#ce1141",
                   "Utah Jazz": "#002b5c",
                   "Washington Wizards": "#002b5c"

                   }


nba_logo_dict = {
    "Atlanta Hawks": "https://i.ibb.co/Bnd73gW/hawks-logo.png",
    "Boston Celtics": "https://i.ibb.co/wymKQGb/celtics-logo.png",
    "Brooklyn Nets": "https://i.ibb.co/SxH3Pdq/nets-logo.png",
    "Charlotte Hornets": "https://i.ibb.co/tKTTfQJ/hornets-logo.png",
    "Chicago Bulls": "https://i.ibb.co/5YKmrmT/bulls-logo.png",
    "Cleveland Cavaliers": "https://i.ibb.co/rZPMPRk/cavs-logo.png",
    "Dallas Mavericks": "https://i.ibb.co/bKH4b25/mavs-logo.png",
    "Denver Nuggets": "https://i.ibb.co/4JSBwWD/nuggets-logo.png",
    "Detroit Pistons": "https://i.ibb.co/WfCpbYy/pistons-logo.png",
    "Golden State Warriors": "https://i.ibb.co/qWwQZdw/warriors-logo.png",
    "Houston Rockets": "https://i.ibb.co/9ZV7t98/rockets-logo.png",
    "Indiana Pacers": "https://i.ibb.co/wKMGfsb/pacers-logo.png",
    "Los Angeles Clippers": "https://i.ibb.co/S3JKLhW/clippers-logo.png",
    "Los Angeles Lakers": "https://i.ibb.co/x2b36Py/lakers-logo.png",
    "Memphis Grizzlies": "https://i.ibb.co/z7C4sBL/grizzlies-logo.png",
    "Miami Heat": "https://i.ibb.co/mt4bQbf/heat-logo.png",
    "Milwaukee Bucks": "https://i.ibb.co/171KQVG/bucks-logo.png",
    "Minnesota Timberwolves": "https://i.ibb.co/1s5H4yW/timberwolves-logo.png",
    "New Orleans Pelicans": "https://i.ibb.co/J7g5zpv/pelicans-logo.png",
    "New York Knicks": "https://i.ibb.co/pKfRhNb/knicks-logo.png",
    "Oklahoma City Thunder": "https://i.ibb.co/R0wPvv5/thunder-logo.png",
    "Orlando Magic": "https://i.ibb.co/7rSsn45/magic-logo.png",
    "Philadelphia 76ers": "https://i.ibb.co/K733rsd/76ers-logo.png",
    "Phoenix Suns": "https://i.ibb.co/0CvLSjc/suns-logo.png",
    "Portland Trail Blazers": "https://i.ibb.co/T1CVdD6/blazers-logo.png",
    "Sacramento Kings": "https://i.ibb.co/dDTHDvZ/kings-logo.png",
    "San Antonio Spurs": "https://i.ibb.co/BKnbDsS/spurs-logo.png",
    "Toronto Raptors": "https://i.ibb.co/3FhV0Y9/raptors-logo.png",
    "Utah Jazz": "https://i.ibb.co/nmjw79s/jazz-logo.png",
    "Washington Wizards": "https://i.ibb.co/hYKZdY9/wizards-logo.png"
}




team_ids_dict = {team['full_name']: team['id'] for team in teams_list}










def choose_basic_stats(team_full_name, season_year, season_type):
    team_stats_basic = TeamInfoCommon(
        league_id="00", team_id=team_ids_dict[team_full_name], season_nullable=season_year - 1, season_type_nullable=season_type)
    return team_stats_basic


def choose_advanced_stats(team_full_name, per_mode, season_type):
    #time.sleep(random_number)
    team_advanced_stats = TeamYearByYearStats(
        league_id="00", per_mode_simple=per_mode, season_type_all_star=season_type, team_id=team_ids_dict[team_full_name])
    return team_advanced_stats
