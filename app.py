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


def balance_teams():
    print("balance_teams")


def app_start():
    print("app_Start")


if __name__ == "__main__":
    players_list = clean_data()
    print(players_list[1])
    # balance_teams()
    # app_start()
