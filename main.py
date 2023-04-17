# WHAT THE FUCK IS GOING ON

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")


def login():
    with open("usernames.txt", 'r') as f:
        for number, line in enumerate(f):
            if str(username) not in line:
                pass
            if str(username) in line:
                line_number = number
                print(line_number)

                with open("passwords.txt", 'r') as f:
                    file_read = f.readlines()
                    file_to_read = file_read[line_number]
                    file_to_read_stripped = file_to_read.strip()
                    output = file_to_read_stripped

                    return output

login()
