# WHAT THE FUCK IS GOING ON

import re


def find_string(input, search_string):
    input.seek(0)
    for line in input:
        line = line.rstrip()
        if re.search(r"\b{}\b".format(search_string), line):
            return True
    return False


def find_string_line(input, search_string):
    input.seek(0)
    for number, line in enumerate(input):
        line = line.rstrip()
        if re.search(r"\b{}\b".format(search_string), line):
            return number
    return False


def read_string_line(input, line_number):
    input.seek(0)
    for i in range(line_number):
        input.readline()
    return input.readline().rstrip()


def edit_string_line(input, line_number, new_string):
    input.seek(0)
    content = input.readlines()
    content[line_number] = new_string + "\n"
    input.seek(0)
    input.writelines(content)


def append_string_line(input, new_string):
    input.seek(0)
    string_format = new_string + '\n'
    content = input.readlines()
    content.append(string_format)
    input.seek(0)
    input.writelines(content)

