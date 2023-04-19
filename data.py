# WHAT THE FUCK IS GOING ON

import re

usernames_file = 'usrnms.bruh'
passwords_file = 'pswds.bruh'

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")


def find_string(input, search_string):
    for number, line in enumerate(input):
        line = line.rstrip()
        if re.search(r"\b{}\b".format(search_string), line):
            return True
        else:
            return False


def find_string_line(input, search_string):
    for number, line in enumerate(input):
        line = line.rstrip()
        if re.search(r"\b{}\b".format(search_string), line):
            return number
        else:
            return False


def read_string_line(input, line_number):
    line = input.readlines()

    return line[line_number]


def login():
    with open(usernames_file, 'r') as a:
        if find_string(a, username) is True:
            print("check1")
            with open(passwords_file, 'r') as s:
                if read_string_line(s, find_string_line(a, username)) == password:
                    print("logged in")


login()
