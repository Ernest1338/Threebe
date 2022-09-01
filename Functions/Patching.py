# This file contains functions that parses user input from pathing
# parameter and are patching given binary.

import sys

def print_help_address(bcolors):
    sys.stderr.write(f"{bcolors.FAIL}ERROR: Wrong address/offset.\n")
    sys.stderr.write(
        f"For help use the --help parameter: {sys.argv[0]} --help{bcolors.RESET}\n")


def print_help_bytes(bcolors):
    sys.stderr.write(f"{bcolors.FAIL}ERROR: Wrong bytes to write.\n")
    sys.stderr.write(
        f"For help use the --help parameter: {sys.argv[0]} --help{bcolors.RESET}\n")


def patch_bin(
        hexdump,
        address,
        bytes_to_write,
        architecture,
        file_name,
        colors):
    bcolors = colors
    offset1 = 134512640
    if (len(bytes_to_write) / 2) == int(len(bytes_to_write) / 2):
        pass
    else:
        print_help_bytes(bcolors)
        return 1
    if architecture == "x86":
        bytes_pointer = int(address, 16) - offset1
        if bytes_pointer < 0 or bytes_pointer > len(hexdump):
            print_help_address(bcolors)
            return 1
    elif architecture == "x86_64":
        bytes_pointer = int(address, 16)
    else:
        pass  # This may be an edge case. Need to do something about that.
    bytes_list = []
    old_bytes = ""
    for i in hexdump:
        bytes_list.append(i)
    for i in range(int(len(bytes_to_write) / 2)):
        try:
            if len(hex(bytes_list[bytes_pointer])[2:]) == 1:
                old_bytes += "0" + str(hex(bytes_list[bytes_pointer])[2:])
            else:
                old_bytes += str(hex(bytes_list[bytes_pointer])[2:])
        except BaseException:
            print_help_address(bcolors)
            return 1
        bytes_list[bytes_pointer] = int(bytes_to_write[i + i:i + i + 2], 16)
        bytes_pointer += 1
    userConfirmation = input(
        f"{bcolors.WARNING}You WILL change the file, do you want to proceed? (Y/n): ")
    if userConfirmation == '' or userConfirmation == "Y" or userConfirmation == "y" or userConfirmation == "Yes" or userConfirmation == "yes":
        file_o = open(file_name, 'wb')
        file_o.write(bytes(bytes_list))
        print(f"{bcolors.OKGREEN}Patching succed.{bcolors.WARNING}")
        print(f"Old bytes: {bcolors.OKBLUE}" + str(''.join(old_bytes)))
        print(
            f"{bcolors.WARNING}New bytes: {bcolors.OKBLUE}" +
            bytes_to_write +
            f"{bcolors.RESET}")
    else:
        print(f"Canceled{bcolors.RESET}")


def patch(hexdump, address, bytes_to_write, architecture, file_name, colors):
    bcolors = colors
    if (len(bytes_to_write) / 2) == int(len(bytes_to_write) / 2):
        pass
    else:
        print_help_bytes(bcolors)
        return 1
    bytes_pointer = int(address, 16)
    bytes_list = []
    old_bytes = ""
    for i in hexdump:
        bytes_list.append(i)
    for i in range(int(len(bytes_to_write) / 2)):
        try:
            if len(hex(bytes_list[bytes_pointer])[2:]) == 1:
                old_bytes += "0" + str(hex(bytes_list[bytes_pointer])[2:])
            else:
                old_bytes += str(hex(bytes_list[bytes_pointer])[2:])
        except BaseException:
            print_help_address(bcolors)
            return 1
        bytes_list[bytes_pointer] = int(bytes_to_write[i + i:i + i + 2], 16)
        bytes_pointer += 1
    userConfirmation = input(
        f"{bcolors.WARNING}You WILL change the file, do you want to proceed? (Y/n): ")
    if userConfirmation == '' or userConfirmation == "Y" or userConfirmation == "y" or userConfirmation == "Yes" or userConfirmation == "yes":
        file_o = open(file_name, 'wb')
        file_o.write(bytes(bytes_list))
        print(f"{bcolors.OKGREEN}Patching succed.{bcolors.WARNING}")
        print(f"Old bytes: {bcolors.OKBLUE}" + str(''.join(old_bytes)))
        print(
            f"{bcolors.WARNING}New bytes: {bcolors.OKBLUE}" +
            bytes_to_write +
            f"{bcolors.RESET}")
    else:
        print(f"Canceled{bcolors.RESET}")
