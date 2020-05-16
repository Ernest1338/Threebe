# This file contain function that returns architecture of given binary file.

import sys

def print_help_filetype():
    sys.stderr.write("ERROR: Unrecognized Filetype.\n")
    sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

def bin_architecture(bytes):
    if ''.join(bytes[1:4])=="454C46":
        filetype = "ELF"
    elif ''.join(bytes[0:2])=="4D5A":
        filetype = "PE"
    else:
        return 1

    if filetype=="ELF":  # ELF - Linux
        if bytes[4]=="01":
            return "x86"
        elif bytes[4]=="02":
            return "x86_64"