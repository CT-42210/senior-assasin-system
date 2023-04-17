# WHAT THE FUCK IS GOING ON

username = input("USERNAME: \n -$")
password = input("PASSWORD: \n -$")

def merit_reader(discord_id):
    d_id = str(discord_id)

    with open("merit.txt", 'r') as f:
        for number, line in enumerate(f):
            if str(d_id) not in line:
                merit_total = 0
            if str(d_id) in line:
                line_number = number

                with open("merit.txt", 'r') as f:
                    file_read = f.readlines()
                    file_int1_read = int(line_number)
                    file_int2_read = (file_int1_read + 1)
                    file_to_read = file_read[file_int2_read]
                    file_to_read_stripped = file_to_read.strip()
                    merit_total = int(file_to_read_stripped)

                    return merit_total