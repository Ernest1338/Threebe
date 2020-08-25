# This is an file containing different functions that extracts information from a executable file.

from Hexdump import bcolors
import sys

def return_filename():
    print("test")
    file_name = sys.argv[2]
    if file_name.find("/")==-1:
        return file_name.split("\\")[-1]
    else:
        return file_name.split("/")[-1]

def bin_get_info(bytes):
    # Type of executable file
    if ''.join(bytes[1:4])=="454C46":
        filetype = "ELF"
        print(f"{bcolors.OKBLUE}"+"File type:           "+f"{bcolors.WARNING}"+filetype+f"{bcolors.ENDC}")
    elif ''.join(bytes[0:2])=="4D5A":
        filetype = "PE"
        print(f"{bcolors.OKBLUE}"+"File Type:           "+f"{bcolors.WARNING}"+filetype+" (Windows Executable)"+f"{bcolors.ENDC}")

    # Magic bytes
    magic = ""
    for i in range(16):
        magic += bytes[i]+" "
    print(f"{bcolors.OKBLUE}"+"Magic bytes:         "+f"{bcolors.WARNING}"+magic+f"{bcolors.ENDC}")

    # Operating System
    if filetype=="ELF":
        os = "Linux"
    elif filetype=="PE":
        os = "Windows"
    print(f"{bcolors.OKBLUE}"+"OS:                  "+f"{bcolors.WARNING}"+os+f"{bcolors.ENDC}")

    # File architecture
    if filetype=="ELF":  # ELF - Linux
        if bytes[4]=="01":
            architecture = "x86"
        elif bytes[4]=="02":
            architecture = "x86_64"
        print(f"{bcolors.OKBLUE}"+"Architecture:        "+f"{bcolors.WARNING}"+architecture+f"{bcolors.ENDC}")

    # File class
    if filetype=="ELF" and architecture=="x86":
        _class = "ELF32"
        print(f"{bcolors.OKBLUE}"+"Class:               "+f"{bcolors.WARNING}"+_class+f"{bcolors.ENDC}")
    elif filetype=="ELF" and architecture=="x86_64":
        _class = "ELF64"
        print(f"{bcolors.OKBLUE}"+"Class:               "+f"{bcolors.WARNING}"+_class+f"{bcolors.ENDC}")

    # Endian type
    if filetype=="ELF":
        if bytes[5]=="01":
            endian = "Little"
        elif bytes[5]=="02":
            endian = "Big"
        print(f"{bcolors.OKBLUE}"+"Endian:              "+f"{bcolors.WARNING}"+endian+f"{bcolors.ENDC}")

    # Entry point address
    if filetype=="ELF":
        if endian=="Little":
            entrypoint = "0x"+bytes[27][1]+bytes[26]+bytes[25]+bytes[24]
        elif endian=="Big":
            entrypoint = "0x"+bytes[24][1]+bytes[25]+bytes[26]+bytes[27]
        print(f"{bcolors.OKBLUE}"+"Entry point address: "+f"{bcolors.WARNING}"+entrypoint+f"{bcolors.ENDC}")

    # ELF version
    if filetype=="ELF":
        elfv = bytes[6][1]
        print(f"{bcolors.OKBLUE}"+"ELF version:         "+f"{bcolors.WARNING}"+elfv+f"{bcolors.ENDC}")