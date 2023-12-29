"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
--------------------------------
"""
from constants import PLAYERS, TEAMS
import copy


def clean_data():
    players_copy = copy.deepcopy(PLAYERS)
    players_cleaned = [{'name': player['name'], 
                            'height': int(player['height'].split()[0]), 
                            'guardians': player['guardians'].split(" and "), 
                            'experience': True if player['experience'].upper() == 'YES' else False} 
                            for player in players_copy]
    return players_cleaned


def balance_teams(players_copy):
    teams_copy = {team: [] for team in copy.deepcopy(TEAMS)}
    
    experienced_players = [player for player in players_copy if player['experience']]
    inexperienced_players = [player for player in players_copy if not player['experience']]

    teams_assigned = {team: experienced_players[i::len(teams_copy)] + 
                      inexperienced_players[i::len(teams_copy)] for i, team in enumerate(teams_copy)}
    return teams_assigned


def app_start():
    print("app_Start")


if __name__ == "__main__":
    players_list = clean_data()
    team_list = balance_teams(players_list)
    app_start()
