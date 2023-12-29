"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
--------------------------------
"""
from constants import PLAYERS, TEAMS
import copy


def clean_data():
    """
    Make a deep copy, clean the data and return
    """
    players_copy = copy.deepcopy(PLAYERS)
    players_cleaned = [{'name': player['name'], 
                        'height': int(player['height'].split()[0]), 
                        'guardians': player['guardians'].split(" and "), 
                        'experience': True if player['experience'].upper() == 'YES' else False} 
                        for player in players_copy]
    return players_cleaned


def balance_teams(players_copy):
    """
    Determine the number of players for each team,
    deep copy the teams constant, sort players by experience, 
    assign players to teams, return the sorted teams
    """
    teams_copy = {team: [] for team in copy.deepcopy(TEAMS)}
    experienced_players = [player for player in players_copy if player['experience']]
    inexperienced_players = [player for player in players_copy if not player['experience']]
    teams_assigned = {team: experienced_players[i::len(teams_copy)] + 
                      inexperienced_players[i::len(teams_copy)] for i, 
                      team in enumerate(teams_copy)}
    return teams_assigned


def display_teams(teams, user_selected_team):
    """
    Display the players on each teams first names.
    """
    players = []
    guardians = []
    for player in teams[user_selected_team]:
        first_name = player['name']
        players.append(first_name)
        guardians.append(player['guardians'])

    print("\nTeam: {} Stats".format(user_selected_team))
    print("-" * 20)
    print("Total Players: {}".format(len(teams[user_selected_team])))
    print("Experienced Players: {}".format(len([player for player in teams[user_selected_team] if player['experience']])))
    print("Inexperienced Players: {}".format(len([player for player in teams[user_selected_team] if not player['experience']])))
    height_list = [player['height'] for player in teams[user_selected_team]]
    print("Average Height: {} {}".format(round(sum(height_list) / len(height_list), 2), "inches"))
    print("\nPlayers on Team:")
    print(", ".join(players))
    print("\nGuardians")
    print(', '.join(', '.join(names) for names in guardians))
    print("\nPress ENTER to continue...\n")
        

def app_start():
    """
    Mainmenu runs until user selects B.
    Submenu for displaying user selected team assignments until user selects enter.
    """
    print("BASKETBALL TEAM STATS TOOL\n")
    print("-" * 4 + "MENU" + "-" * 4)
    user_input = ""
    while user_input.upper() != "B":
        print("\nHere are your choices:\n A) Display Team Stats\n B) Quit\n")
        user_input = input("Enter an option: ")
        if user_input.upper() == "A":
            user_selected_team = ""
            print("\nA) Panthers\nB) Bandits\nC) Warriors\n")
            while True:
                user_selected_team = input("Enter an option: ")
                if user_selected_team.upper() == "A":
                    display_teams(team_list, "Panthers")
                elif user_selected_team.upper() == "B":
                    display_teams(team_list, "Bandits")
                elif user_selected_team.upper() == "C":
                    display_teams(team_list, "Warriors")
                elif user_selected_team == "":
                    break
                else:
                    print("\nPlease Enter a Menu Option\n")
        else:
            print("\nPlease Enter a Menu Option")


if __name__ == "__main__":
    players_list = clean_data()
    team_list = balance_teams(players_list)
    app_start()
