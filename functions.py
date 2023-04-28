# IM GOING TO FUCKING KILL MYSELF

import database

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")

username_file = open('database/usernames.not.a.database.file', 'r+')
password_file = open('database/passwords.not.a.database.file', 'r+')
team_id_file = open('database/team_ids.not.a.database.file', 'r+')
team_names_file = open('database/team_names.not.a.database.file', 'r+')
team_targets_file = open('database/team_targets.not.a.database.file', 'r+')


def login():
    line_number = database.find_string_line(username_file, username)
    if line_number is False:
        print("Username not found.")
        return
    username_file.seek(0)
    password_line = database.read_string_line(password_file, line_number)
    if password_line == password:
        print("Logged in.")
    else:
        print("Incorrect password.")


def teams():
    line_number = database.find_string_line(username_file, username)
    print(line_number)
    if line_number is not False:
        team_id_line = database.read_string_line(team_id_file, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_name_line = database.read_string_line(team_names_file, (int(team_id_line) - 1))
                print(team_name_line)
            except ValueError:
                print("ValueError")


def targets():
    line_number = database.find_string_line(username_file, username)
    print(line_number)
    if line_number is not False:
        team_id_line = database.read_string_line(team_id_file, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_target_line = database.read_string_line(team_targets_file, (int(team_id_line) - 1))
                print(team_target_line)
                target_name_line = database.read_string_line(team_names_file, (int(team_target_line) - 1))
                print(f"your ops are team {team_target_line}. they are called {target_name_line}")
            except ValueError:
                print("ValueError")


def account_creator():
    new_username = input("What do you want your username to be? \n(No spaces please)\n -$")
    new_password = input("What do you want your username to be? \n(No spaces please)\n -$")

    new_team_id = '0'

    if database.find_string(username_file, new_username) is False:
        database.append_string_line(username_file, new_username)
        database.append_string_line(password_file, new_password)
        database.append_string_line(team_id_file, new_team_id)

        print(f"user created.\nUsername: {new_username}\nPassword: {new_password}\nTeam: Unassigned")
    else:
        print("error")


def team_creater():
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

team_creater()

username_file.close()
password_file.close()
team_id_file.close()
team_names_file.close()
team_targets_file.close()
