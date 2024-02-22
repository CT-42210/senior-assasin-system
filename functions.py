# IM GOING TO FUCKING KILL MYSELF

import database

username_file = open('database/usernames.not.a.database.file', 'r+')
password_file = open('database/passwords.not.a.database.file', 'r+')
team_id_file = open('database/team_ids.not.a.database.file', 'r+')
team_names_file = open('database/team_names.not.a.database.file', 'r+')
team_targets_file = open('database/team_targets.not.a.database.file', 'r+')
team_health_file = open('database/team_health.not.a.database.file', 'r+')
player_health_file = open('database/player_health.not.a.database.file', 'r+')
user_address_file = open('database/user_adresses.not.a.database.file', 'r+')


def login(username, password):
    line_number = database.find_string_line(username_file, username)
    if line_number is False:
        print("Username not found.")
        return
    username_file.seek(0)
    password_line = database.read_string_line(password_file, line_number[0])
    if password_line == password:
        print("Logged in.")
        return True
    else:
        print("Incorrect password.")
        return False


def team_data(username):
    return_list = []

    line_number = database.find_string_line(username_file, username)

    player_health = database.read_string_line(player_health_file, line_number[0])
    player_address = database.read_string_line(user_address_file, line_number[0])
    if line_number is not False:
        team_id_line = database.read_string_line(team_id_file, line_number[0])
        if team_id_line != '':
            try:
                team_name_line = database.read_string_line(team_names_file, (int(team_id_line) - 1))
                team_user_lines = database.find_string_line(team_id_file, int(team_id_line))
                for user_line in team_user_lines:
                    if user_line == line_number[0]:
                        pass
                    else:
                        teammate_name = database.read_string_line(username_file, int(user_line))
                        teammate_health = database.read_string_line(player_health_file, int(user_line))
                        teammate_address = database.read_string_line(user_address_file, int(user_line))

                        return_list.append(team_name_line)
                        return_list.append(teammate_name)
                        return_list.append(teammate_health)
                        return_list.append(player_health)
                        return_list.append(player_address)
                        return_list.append(teammate_address)
                        return return_list
            except ValueError:
                print("ValueError")
                return False


def targets(username):
    return_list = []
    line_number = database.find_string_line(username_file, username)
    if line_number is not False:
        team_id_line = database.read_string_line(team_id_file, line_number[0])
        if team_id_line != '':
            try:
                team_target_line = database.read_string_line(team_targets_file, (int(team_id_line) - 1))
                target_team_name = database.read_string_line(team_names_file, (int(team_target_line) - 1))
                target_team_health = database.read_string_line(team_health_file, (int(team_target_line) - 1))
                opponent_user_ids = database.find_string_line(team_id_file, team_target_line)

                if opponent_user_ids is not False:
                    first_opponent = database.read_string_line(username_file, opponent_user_ids[0])
                    second_opponent = database.read_string_line(username_file, opponent_user_ids[1])
                    first_opponent_health = database.read_string_line(username_file, opponent_user_ids[0])
                    second_opponent_health = database.read_string_line(username_file, opponent_user_ids[1])
                    first_opponent_address = database.read_string_line(user_address_file, opponent_user_ids[0])
                    second_opponent_address = database.read_string_line(user_address_file, opponent_user_ids[1])

                    try:
                        return_list.append(target_team_name)
                        return_list.append(first_opponent)
                        return_list.append(second_opponent)

                        return_list.append(target_team_health)
                        return_list.append(first_opponent_health)
                        return_list.append(second_opponent_health)
                        return_list.append(first_opponent_address)
                        return_list.append(second_opponent_address)

                    except IndexError:
                        print("Index Error when appending opponent list")
                    return return_list
            except ValueError:
                print("ValueError")


def teammate_data(username):
    line_number = database.find_string_line(username_file, username)
    if line_number is not False:
        team_id_line = database.read_string_line(team_id_file, line_number[0])
        if team_id_line != '':
            try:
                team_name_line = database.read_string_line(team_names_file, (int(team_id_line) - 1))
                return team_name_line
            except ValueError:
                print("ValueError")


def total_team_data():
    return_list = []

    total_team_number = database.last_line_finder(team_names_file) + 1
    total_player_number = database.last_line_finder(username_file) + 1

    dead_teams_number = database.find_string_matches(team_health_file, "dead")
    living_teams_number = total_team_number - dead_teams_number

    living_players_number = database.find_string_matches(player_health_file, "alive")

    return_list.append(total_team_number)
    return_list.append(total_player_number)
    return_list.append(living_teams_number)
    return_list.append(living_players_number)

    return return_list


def account_creator(new_username, new_password):

    new_team_id = '0'

    if database.find_string(username_file, new_username) is False:
        database.append_string_line(username_file, new_username)
        database.append_string_line(password_file, new_password)
        database.append_string_line(team_id_file, new_team_id)

        print(f"user created.\nUsername: {new_username}\nPassword: {new_password}\nTeam: Unassigned")
    else:
        print("error")


def team_creater(username, password):
    new_team_name = input("Enter the new teams name:\n -$")
    first_team_member = input("Enter the First Members User ID:\n -$")
    second_team_member = input("Enter the Second Members User ID:\n -$")

    new_team_id = database.last_line_finder(team_names_file)

    if database.read_string_line(team_id_file, int(first_team_member)) == '0':
        if database.read_string_line(team_id_file, int(second_team_member)) == '0':
            verification = input(f"creating new team\nTeam Name: {new_team_name}\n"
                                 f"members: {database.read_string_line(username_file, int(first_team_member))}, "
                                 f"{database.read_string_line(username_file, int(first_team_member))}\n"
                                 f"Targets: Undefined\n"
                                 f"Are you sure? [Y, n]\n -$")
            if verification == 'y' or 'Y':
                database.edit_string_line(team_id_file, int(first_team_member), new_team_id)
                database.edit_string_line(team_id_file, int(second_team_member), new_team_id)
                database.append_string_line(team_names_file, new_team_name)
                database.append_string_line(team_targets_file, '0')


def close():
    username_file.close()
    password_file.close()
    team_id_file.close()
    team_names_file.close()
    team_targets_file.close()
