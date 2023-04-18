# WHAT THE FUCK IS GOING ON

import re

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")


def find_string(input, string):
    for number, line in enumerate(input):
        line = line.rstrip()
        if re.search(r"\b{}\b".format(string), line):
            return True
        else:
            return False


def find_string_line(input, string):
    for number, line in enumerate(input):
        line = line.rstrip()
        if re.search(r"\b{}\b".format(string), line):
            return number
        else:
            return False

def read_string_line(input, line_number):
    for number, line in enumerate(input):
        return line[line_number]


def login():
    with open('usernames.txt', 'r') as a:
        if find_string(a) is True:
            with open('passwords.txt', 'r') as s:
                if find_string_line(s) is True:
                    pass


with open('usernames.txt', 'r') as a:
    read_string_line(a, 1)
