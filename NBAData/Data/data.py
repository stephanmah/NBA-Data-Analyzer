from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, TeamInfoCommon, TeamYearByYearStats
import pandas as pd


class DataManager:
    def __init__(self):
        self.active_players_DF = players.get_active_players()
        self.inactive_players_DF = players.get_inactive_players()
        self.teams_DF = self.get_teams()

        self.season_stat_type_to_id = {
            "Regular Season": 0,
            "Career Totals": 1,
            "Playoffs": 2,
            "Playoffs Totals": 3,
            "All Star Games": 4,
            "All Star Totals": 5,
        }
        self.nba_logo_dict = {
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

        self.nba_colors_dict = {"Atlanta Hawks": "#e03a3e",
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

    def get_active_players(self):
        active_players_data = players.get_active_players()
        return pd.DataFrame(active_players_data)

    def get_inactive_players(self):
        inactive_players_data = players.get_inactive_players()

        return pd.DataFrame(inactive_players_data)

    def get_player_id(self,player_name):
        active_player_data = players.get_active_players()
        player_to_id_map = {active_player["full_name"]: active_player[id] for active_player in active_player_data}
        return player_to_id_map[player_name]



    def get_teams(self):
        teams_data = teams.get_teams()
        return pd.DataFrame(teams_data)
