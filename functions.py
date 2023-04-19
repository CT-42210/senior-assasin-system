# IM GOING TO FUCKING KILL MYSELF

import data

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")

username_file = open('data/usernames.bruh', 'r+')
password_file = open('data/passwords.bruh', 'r+')
team_id_file = open('data/team_ids.bruh', 'r+')
team_names_file = open('data/team_names.bruh', 'r+')
team_targets_file = open('data/team_targets.bruh', 'r+')


def login():
    line_number = data.find_string_line(username_file, username)
    if line_number is False:
        print("Username not found.")
        return
    username_file.seek(0)
    password_line = data.read_string_line(password_file, line_number)
    if password_line == password:
        print("Logged in.")
    else:
        print("Incorrect password.")


def teams():
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


def targets():
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


def account_creator():
    new_username = input("What do you want your username to be? \n(No spaces please)\n -$")
    new_password = input("What do you want your username to be? \n(No spaces please)\n -$")

    new_team_id = '0'

    if data.find_string(username_file, new_username) is False:
        data.append_string_line(username_file, new_username)
        data.append_string_line(password_file, new_password)
        data.append_string_line(team_id_file, new_team_id)

        print(f"user created.\nUsername: {new_username}\nPassword: {new_password}\nTeam: Unassigned")
    else:
        print("error")

account_creator()

username_file.close()
password_file.close()
team_id_file.close()
team_names_file.close()
team_targets_file.close()
