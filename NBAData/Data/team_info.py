from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamInfoCommon, TeamYearByYearStats
import pandas as pd

teams_list = teams.get_teams()

team_list_DF = pd.DataFrame(teams.get_teams())






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
                 "Atlanta Hawks": "images/hawks_logo.png",
                 "Boston Celtics": "images/celtics_logo.png",
                 "Brooklyn Nets": "images/nets_logo.png",
                 "Charlotte Hornets": "images/hornets_logo.png",
                 "Chicago Bulls": "images/bulls_logo.png",
                 "Cleveland Cavaliers": "images/cavs_logo.png",
                 "Dallas Mavericks": "images/mavs_logo.png",
                 "Denver Nuggets": "images/nuggets_logo.png",
                 "Detroit Pistons": "images/pistons_logo.png",
                 "Golden State Warriors": "images/warriors_logo.png",
                 "Houston Rockets": "images/rockets_logo.png",
                 "Indiana Pacers": "images/pacers_logo.png",
                 "Los Angeles Clippers": "images/clippers_logo.png",
                 "Los Angeles Lakers": "images/lakers_logo.png",
                 "Memphis Grizzlies": "images/grizzlies_logo.png",
                 "Miami Heat": "images/heat_logo.png",
                 "Milwaukee Bucks": "images/bucks_logo.png",
                 "Minnesota Timberwolves": "images/timberwolves_logo.png",
                 "New Orleans Pelicans": "images/pelicans_logo.png",
                 "New York Knicks": "images/knicks_logo.png",
                 "Oklahoma City Thunder": "images/thunder_logo.png",
                 "Orlando Magic": "images/magic_logo.png",
                 "Philadelphia 76ers": "images/76ers_logo.png",
                 "Phoenix Suns": "images/suns_logo.png",
                 "Portland Trail Blazers": "images/blazers_logo.png",
                 "Sacramento Kings": "images/kings_logo.png",
                 "San Antonio Spurs": "images/spurs_logo.png",
                 "Toronto Raptors": "images/raptors_logo.png",
                 "Utah Jazz": "images/jazz_logo.png",
                 "Washington Wizards": "images/wizards_logo.png"

                 }



team_ids_dict = {team['full_name']: team['id'] for team in teams_list}










def choose_basic_stats(team_full_name, season_year, season_type):

    team_stats_basic = TeamInfoCommon(
        league_id="00", team_id=team_ids_dict[team_full_name], season_nullable=season_year - 1, season_type_nullable=season_type)
    return team_stats_basic


def choose_advanced_stats(team_full_name, per_mode, season_type):
    team_advanced_stats = TeamYearByYearStats(
        league_id="00", per_mode_simple=per_mode, season_type_all_star=season_type, team_id=team_ids_dict[team_full_name])
    return team_advanced_stats
