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
    player_names = []
    player_heights = []
    guardians_list = []
    total_players = len(teams[selected_team])  
    experienced_players = len([player for player in teams[selected_team] if player['experience']])
    inexperienced_players = len([player for player in teams[selected_team] if not player['experience']])
    # Populate Variables
    for player in teams[selected_team]:
        first_name = player['name']
        height = player['height']
        guardians = player['guardians']
        player_names.append(first_name)
        player_heights.append(height)
        guardians_list.append(guardians)
    # Dependant Variables
    flat_guardians_list = [name for sublist in guardians_list for name in sublist]
    average_height = round(sum(player_heights) / len(player_heights), 2)
    # Return  
    team_stats = {
        'total_players': total_players,
        'experienced_players': experienced_players,
        'inexperienced_players': inexperienced_players,
        'average_height': average_height,
        'player_names': player_names,
        'guardians': flat_guardians_list
    }
    return team_stats


def display_teams(teams, selected_team):
    """
    Display the team stats.
    """
    team_stats = team_calculations(teams, selected_team)
    print("\nTeam: {} Stats".format(selected_team))
    print("-" * 20)
    print("Total Players: {}".format(team_stats['total_players']))
    print("Experienced Players: {}".format(team_stats['experienced_players']))
    print("Inexperienced Players: {}".format(team_stats['inexperienced_players']))
    print("Average Height: {} {}".format(team_stats['average_height'], "inches"))
    print("\nPlayers on Team:")
    print(', '.join(team_stats['player_names']))
    print("\nGuardians")
    print(', '.join(team_stats['guardians']))
    print("\nPress ENTER to continue...\n")


def app_start(teams):
    """
    Main menu runs until user selects B.
    Submenu displays user selected team until user selects enter.
    """
    print("BASKETBALL TEAM STATS TOOL\n")
    print("-" * 4 + "MENU" + "-" * 4)
    user_input = ""
    while True:
        print("\nHere are the choices:\n A) Display Team Stats\n B) Quit\n")
        user_input = input("Enter a Choice: ")
        if user_input.upper() == "A":
            user_selected_team = ""
            print("\nA) Panthers\nB) Bandits\nC) Warriors\n")
            while True:
                user_selected_team = input("Enter an Team or use Enter to return: ")
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
        elif user_input.upper() == "B":
            print("Goodbye!")
            break
        else:
            print("\nPlease Enter a Menu Option")


def save_data(team_list):
    """
    Save Data to Teams Data Structure
    """
    for team_name in ['Panthers', 'Bandits', 'Warriors']:
        team_stats = team_calculations(team_list, team_name)
        stats = {
            'experienced_players': team_stats['experienced_players'],
            'inexperienced_players': team_stats['inexperienced_players'],
            'average_height': team_stats['average_height'],
        }
        team_list[team_name].append(stats)
        

if __name__ == "__main__":
    players_list = clean_data()
    team_list = balance_teams(players_list)
    app_start(team_list)
    save_data(team_list)
