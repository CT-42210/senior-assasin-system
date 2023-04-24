# IM GOING TO FUCKING KILL MYSELF

import data


username_file = open('data/usernames.not.a.database.file', 'r+')
password_file = open('data/passwords.not.a.database.file', 'r+')
team_id_file = open('data/team_ids.not.a.database.file', 'r+')
team_names_file = open('data/team_names.not.a.database.file', 'r+')
team_targets_file = open('data/team_targets.not.a.database.file', 'r+')


def login(username, password):
    line_number = data.find_string_line(username_file, username)
    if line_number is False:
        print("Username not found.")
        return
    username_file.seek(0)
    password_line = data.read_string_line(password_file, line_number)
    if password_line == password:
        print("Logged in.")
        return True
    else:
        print("Incorrect password.")
        return False


def teams(username, password):
    line_number = data.find_string_line(username_file, username)
    print(line_number)
    if line_number is not False:
        team_id_line = data.read_string_line(team_id_file, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_name_line = data.read_string_line(team_names_file, (int(team_id_line) - 1))
                print(team_name_line)
            except ValueError:
                print("ValueError")


def targets(username, password):
    line_number = data.find_string_line(username_file, username)
    print(line_number)
    if line_number is not False:
        team_id_line = data.read_string_line(team_id_file, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_target_line = data.read_string_line(team_targets_file, (int(team_id_line) - 1))
                print(team_target_line)
                target_name_line = data.read_string_line(team_names_file, (int(team_target_line) - 1))
                print(f"your ops are team {team_target_line}. they are called {target_name_line}")
            except ValueError:
                print("ValueError")


def account_creator(username, password):
    new_username = input("What do you want your username to be? \n(No spaces please)\n -$")
    new_password = input("What do you want your password to be? \n(No spaces please)\n -$")

    new_team_id = '0'

    if data.find_string(username_file, new_username) is False:
        data.append_string_line(username_file, new_username)
        data.append_string_line(password_file, new_password)
        data.append_string_line(team_id_file, new_team_id)

        print(f"user created.\nUsername: {new_username}\nPassword: {new_password}\nTeam: Unassigned")
    else:
        print("error")


def team_creater(username, password):
    new_team_name = input("Enter the new teams name:\n -$")
    first_team_member = input("Enter the First Members User ID:\n -$")
    second_team_member = input("Enter the Second Members User ID:\n -$")

    new_team_id = data.last_line_finder(team_names_file)

    if data.read_string_line(team_id_file, int(first_team_member)) == '0':
        if data.read_string_line(team_id_file, int(second_team_member)) == '0':
            verification = input(f"creating new team\nTeam Name: {new_team_name}\n"
                                 f"members: {data.read_string_line(username_file, int(first_team_member))}, "
                                 f"{data.read_string_line(username_file, int(first_team_member))}\n"
                                 f"Targets: Undefined\n"
                                 f"Are you sure? [Y, n]\n -$")
            if verification == 'y' or 'Y':

                data.edit_string_line(team_id_file, int(first_team_member), new_team_id)
                data.edit_string_line(team_id_file, int(second_team_member), new_team_id)
                data.append_string_line(team_names_file, new_team_name)
                data.append_string_line(team_targets_file, '0')

def close():
    username_file.close()
    password_file.close()
    team_id_file.close()
    team_names_file.close()
    team_targets_file.close()
