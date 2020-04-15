import constants
import random 
import copy

def clean_data():
    new_players_list = copy.deepcopy(constants.PLAYERS)
    for player in new_players_list:
        for key, value in player.items():
            if key == "experience":
                if value == "NO":
                    player[key] = False
                else:
                    player[key] = True
            if key == "height":
                height_list = value.split(" ")
                height = int(height_list[0])
                player[key] = height
    return (new_players_list)


def create_player_list(players):
    experienced_players = []
    inexperienced_players = []
    for player in players:
        for key, value in player.items():
            if key == "experience":
                if value == False:
                    inexperienced_players.append(player)
                else:
                    experienced_players.append(player)
    return experienced_players, inexperienced_players

def populate_teams(experienced_players, inexperienced_players):
    panthers = []
    bandits = []
    warriors = []
    players_left = True

    while players_left:
        # ADDING TO PANTHERS
        experienced_index = random.randint(0, len(experienced_players) - 1)
        inexperienced_index = random.randint(0, len(inexperienced_players) - 1)
        panthers.append(experienced_players[experienced_index])
        del experienced_players[experienced_index]
        panthers.append(inexperienced_players[inexperienced_index])
        del inexperienced_players[inexperienced_index]
        # ADDING TO BANDITS
        experienced_index = random.randint(0, len(experienced_players) - 1)
        inexperienced_index = random.randint(0, len(inexperienced_players) - 1)
        bandits.append(experienced_players[experienced_index])
        del experienced_players[experienced_index]
        bandits.append(inexperienced_players[inexperienced_index])
        del inexperienced_players[inexperienced_index]
        # ADDING TO WARRIORS
        experienced_index = random.randint(0, len(experienced_players) - 1)
        inexperienced_index = random.randint(0, len(inexperienced_players) - 1)
        warriors.append(experienced_players[experienced_index])
        del experienced_players[experienced_index]
        warriors.append(inexperienced_players[inexperienced_index])
        del inexperienced_players[inexperienced_index]
        if len(experienced_players) > 0:
            continue
        else:
            players_left = False

    return panthers, bandits, warriors

def display_teams():
    print("\n")
    print("1. Panthers")
    print("2. Bandits")
    print("3. Warriors")
    print("\n")

def display_team(team_name, num_players, players_list):
    print("\n")
    print("Team: {} stats.".format(team_name))
    print("Total players: {}".format(num_players))
    print("\n")
    print("Players on team: \n")
    print("'".join(players_list))
    print("\n")

def get_player_names(player_list):
    player_names = []
    for val in player_list:
        for key, value in val.items():
            if key == "name":
                player_names.append(value)
    return player_names


if __name__ == "__main__":
    experienced, inexperienced = create_player_list(clean_data())
    panthers_players, bandits_players, warriors_players = populate_teams(experienced, inexperienced)
    print("Basketball Teams Stats Tool")
    print("---------------------------")
    print("Main Menu:")
    print("\n")
    print("Please choose an option")
    print("\n")
    print("1. Display Team Stats")
    print("2. Quit")
    print("\n")
    not_quit = True
    in_teams = False


    while not_quit:
        try:
            selection = int(input("Please make a selection: "))
        except:
            print("Please choose only 1 or 2")
            continue
        if selection > 2 or selection < 1:
            print("Please choose either 1 or 2")
            continue
        elif selection == 1:
            in_teams = True
            # Loop for choosing between teams
            while in_teams:
                display_teams()
                try:
                    selection =int(input("Please make a selection: "))
                except:
                    print("Please choose only 1,2 or 3")
                    continue
                if selection < 1 or selection > 3:
                    print("Please choose one of the menu options.")
                    continue
                if selection == 1:
                    display_team("Panthers", len(panthers_players), get_player_names(panthers_players))
                elif selection == 2:
                    display_team("Bandits", len(bandits_players), get_player_names(bandits_players))
                elif selection == 3:
                    display_team("Warriors", len(warriors_players), get_player_names(warriors_players))
                not_again = True
                # Loop for choosing between teams again or quitting
                while not_again:
                    would_continue = input("Would you like to continue? (y)es or (n)o?")
                    if would_continue == "Y" or would_continue == "y":
                        not_again = False
                    elif would_continue == "N" or would_continue == "n":
                        not_again = False
                        in_teams = False
                        not_quit = False
                        print("Thanks for checking out Basketball stats!")
                    else:
                        print("Please choose either y for yes or n for no.")
        elif selection == 2:
            print("Okay goodbye!")
            not_quit = False








