# This script is to used by only for Syariffudin #
# This simple script is to get user input (arbitrary data) -
# and write it to a file #
# December 2016 #
import os

print("Welcome!")
user_inputs_list = list()

# to append to a file with input strings
def write_to_file(filename, input_tofile):
    with open(filename, "a") as out_file:
                out_file.write(input_tofile)

# get the directory of the file location in
def get_file_location(filename):
    return os.path.dirname(os.path.realpath(filename))

while True:
    user_input = input('Enter data, type #stop to stop: \n')
    if "#stop" in user_input:
        break
    else:
        user_inputs_list.append(user_input)
        user_inputs_list.append("\n")

while True:
    save_file_confrm = input ("Do you want to save those input to a file? Y/N\n")
    if "Y" or "y" in save_file_confrm:
        filename = input("Enter your filename to save the data you've input:\n")
        for item in user_inputs_list:
            write_to_file(filename, item)
        print(filename + " saved at: " + get_file_location(filename))
        break
    elif "N" or "n" in save_file_confrm:
        print("oh... well then byee...")
    else:
        print("Invalid input!")

print("Thank you...")
#end

