# IM GOING TO FUCKING KILL MYSELF

import data

usernames_file = 'data/usernames.bruh'
passwords_file = 'data/passwords.bruh'
team_id_file = 'data/team_ids.bruh'
team_name_file = 'data/team_names.bruh'
team_targets_file = 'data/team_targets.bruh'

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")

a = open(usernames_file, 'r')
s = open(passwords_file, 'r')
f = open(team_id_file, 'r')
d = open(team_name_file, 'r')
z = open(team_targets_file, 'r')

def login():
    line_number = data.find_string_line(a, username)
    if line_number is False:
        print("Username not found.")
        return
    a.seek(0)
    password_line = data.read_string_line(s, line_number)
    if password_line == password:
        print("Logged in.")
    else:
        print("Incorrect password.")


def teams():
    line_number = data.find_string_line(a, username)
    print(line_number)
    if line_number is not False:
        team_id_line = data.read_string_line(f, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_name_line = data.read_string_line(d, (int(team_id_line) - 1))
                print(team_name_line)
            except ValueError:
                print("ValueError")


def targets():
    line_number = data.find_string_line(a, username)
    print(line_number)
    if line_number is not False:
        team_id_line = data.read_string_line(f, line_number)
        print(team_id_line)
        if team_id_line != '':
            try:
                team_target_line = data.read_string_line(z, (int(team_id_line) - 1))
                print(team_target_line)
                target_name_line = data.read_string_line(d, (int(team_target_line) - 1))
                print(f"your ops are team {team_target_line}. they are called {target_name_line}")
            except ValueError:
                print("ValueError")

targets()

def account_creator():
    new_username = input("What do you want your username to be? \n -$")
    new_password = input("What do you want your username to be? \n -$")

    with open(usernames_file, 'r') as a:
        with open(passwords_file, 'r') as s:
            with open(team_id_file, 'r') as f:


a.close()
s.close()
f.close()
d.close()
z.close()
