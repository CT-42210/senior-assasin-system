# IM GOING TO FUCKING KILL MYSELF

import data

usernames_file = 'data/usernames.bruh'
passwords_file = 'data/passwords.bruh'
team_id_file = 'data/team_ids.bruh'
team_name_file = 'data/team_names.bruh'

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")


def login():
    with open(usernames_file, 'r') as a:
        line_number = data.find_string_line(a, username)
        if line_number is False:
            print("Username not found.")
            return
        a.seek(0)
        with open(passwords_file, 'r') as s:
            password_line = data.read_string_line(s, line_number)
            if password_line == password:
                print("Logged in.")
            else:
                print("Incorrect password.")


def teams():
    with open(usernames_file, 'r') as a:
        line_number = data.find_string_line(a, username)
        print(line_number)
        if line_number is not False:
            with open(team_id_file, 'r') as f:
                team_id_line = data.read_string_line(f, line_number)
                print(team_id_line)
                if team_id_line != '':
                    try:
                        with open(team_name_file, 'r') as d:
                            team_name_line = data.read_string_line(d, (int(team_id_line) - 1))
                            print(team_name_line)
                    except ValueError:
                        print("ValueError")


teams()
