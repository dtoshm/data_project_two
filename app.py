"""
Data Analysis Techdegree
Project 2 - A Basketball Stats Tool
-----------------------------------
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


def balance_teams(players):
    """
    Determine the number of players for each team,
    deep copy the teams constant, sort players by experience, 
    assign players to teams, return the sorted teams
    """
    teams_copy = {team: [] for team in copy.deepcopy(TEAMS)}
    experienced_players = [player for player in players if player['experience']]
    inexperienced_players = [player for player in players if not player['experience']]
    teams_assigned = {team: experienced_players[i::len(teams_copy)] + 
                      inexperienced_players[i::len(teams_copy)] for i, 
                      team in enumerate(teams_copy)}
    return teams_assigned


def team_calculations(teams, selected_team):
    """
    Calculate and return various statistics for a selected team.
    """
    players = []
    for player in teams[selected_team]:
        first_name = player['name']
        height = player['height']
        guardians = player['guardians']
        players.append((first_name, height, guardians))
    experienced_players = len([player for player in teams[selected_team] if player['experience']])
    inexperienced_players = len([player for player in teams[selected_team] if not player['experience']])
    total_players = len(teams[selected_team])
    player_heights = [player[1] for player in players]    
    average_height = round(sum(player_heights) / len(player_heights), 2)
    sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
    player_names = [player[0] for player in sorted_players]
    guardians = [item[2] for item in players]
    teams[selected_team].append({'experience_players': experienced_players})
    teams[selected_team].append({'inexperienced_players': inexperienced_players})
    teams[selected_team].append({'average_height': average_height})
    return total_players, experienced_players, inexperienced_players, average_height, player_names, guardians


def display_teams(teams, selected_team):
    """
    Display the team stats.
    """
    total_players, experienced_players, inexperienced_players, average_height, player_names, guardians = team_calculations(teams, selected_team)
    print("\nTeam: {} Stats".format(selected_team))
    print("-" * 20)
    print("Total Players: {}".format(total_players))
    print("Experienced Players: {}".format(experienced_players))
    print("Inexperienced Players: {}".format(inexperienced_players))
    print("Average Height: {} {}".format(average_height, "inches"))
    print("\nPlayers on Team:")
    print(', '.join(player_names))
    print("\nGuardians")
    print(', '.join(str(player) for players in guardians for player in players))
    print("\nPress ENTER to continue...\n")


def app_start(teams):
    """
    Main menu runs until user selects B.
    Submenu displays user selected team until user selects enter.
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
                    display_teams(teams, "Panthers")
                elif user_selected_team.upper() == "B":
                    display_teams(teams, "Bandits")
                elif user_selected_team.upper() == "C":
                    display_teams(teams, "Warriors")
                elif user_selected_team == "":
                    break
                else:
                    print("\nPlease Enter a Menu Option\n")
        else:
            print("\nPlease Enter a Menu Option")


if __name__ == "__main__":
    players_list = clean_data()
    team_list = balance_teams(players_list)
    app_start(team_list)
