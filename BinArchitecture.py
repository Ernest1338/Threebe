# This file contain function that returns architecture of given binary file.

def bin_architecture(bytes):
    if ''.join(bytes[1:4])=="454C46":
        filetype = "ELF"
    elif ''.join(bytes[0:2])=="4D5A":
        filetype = "PE"

    if filetype=="ELF":  # ELF - Linux
        if bytes[4]=="01":
            return "x86"
        elif bytes[4]=="02":
            return "x86_64"
