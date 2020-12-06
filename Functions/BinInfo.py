# This is an file containing different functions that extracts information from a executable file.

from Functions.Colors import bcolors
import sys

def return_filename():
    file_name = sys.argv[2]
    if file_name.find("/")==-1:
        return file_name.split("\\")[-1]
    else:
        return file_name.split("/")[-1]

def bin_get_info(bytes, clean):
    if clean:
        colors=['','','']
    else:
        colors=['\033[94m', '\033[93m', '\033[0m']
    # File name
    print(f"{colors[0]}"+"File name:           "+f"{colors[1]}"+str(return_filename())+f"{colors[2]}")

    # Format of executable file
    if ''.join(bytes[1:4])=="454C46":
        fileformat = "ELF"
        print(f"{colors[0]}"+"File format:         "+f"{colors[1]}"+fileformat+f"{colors[2]}")
    elif ''.join(bytes[0:2])=="4D5A":
        fileformat = "PE"
        print(f"{colors[0]}"+"File format:         "+f"{colors[1]}"+fileformat+" (Windows Executable)"+f"{colors[2]}")
    else:
        fileformat = "Unknown"
        print(f"{colors[0]}"+"File format:         "+f"{colors[1]}"+fileformat+f"{colors[2]}")

    # File type
    if fileformat == "ELF" or fileformat == "PE":
        filetype = "EXEC (Executable file)"
        print(f"{colors[0]}"+"File type:           "+f"{colors[1]}"+filetype+f"{colors[2]}")
    else:
        filetype = "File"
        print(f"{colors[0]}"+"File type:           "+f"{colors[1]}"+filetype+f"{colors[2]}")

    # Magic bytes
    magic = ""
    for i in range(16):
        magic += bytes[i]+" "
    print(f"{colors[0]}"+"Magic bytes:         "+f"{colors[1]}"+magic+f"{colors[2]}")

    # Operating System
    if fileformat=="ELF":
        os = "Linux"
    elif fileformat=="PE":
        os = "Windows"
    else:
        os = "Unknown"
    print(f"{colors[0]}"+"OS:                  "+f"{colors[1]}"+os+f"{colors[2]}")

    # File architecture
    if fileformat=="ELF":  # ELF - Linux
        if bytes[4]=="01":
            architecture = "x86"
        elif bytes[4]=="02":
            architecture = "x86_64"
        print(f"{colors[0]}"+"Architecture:        "+f"{colors[1]}"+architecture+f"{colors[2]}")

    # File class
    if fileformat=="ELF" and architecture=="x86":
        _class = "ELF32"
        print(f"{colors[0]}"+"Class:               "+f"{colors[1]}"+_class+f"{colors[2]}")
    elif fileformat=="ELF" and architecture=="x86_64":
        _class = "ELF64"
        print(f"{colors[0]}"+"Class:               "+f"{colors[1]}"+_class+f"{colors[2]}")

    # Endian type
    if fileformat=="ELF":
        if bytes[5]=="01":
            endian = "Little"
        elif bytes[5]=="02":
            endian = "Big"
        print(f"{colors[0]}"+"Endian:              "+f"{colors[1]}"+endian+f"{colors[2]}")

    # Entry point address
    if fileformat=="ELF":
        if endian=="Little":
            entrypoint = "0x"+bytes[27][1]+bytes[26]+bytes[25]+bytes[24]
        elif endian=="Big":
            entrypoint = "0x"+bytes[24][1]+bytes[25]+bytes[26]+bytes[27]
        print(f"{colors[0]}"+"Entry point address: "+f"{colors[1]}"+entrypoint+f"{colors[2]}")

    # ELF version
    if fileformat=="ELF":
        elfv = bytes[6][1]
        print(f"{colors[0]}"+"ELF version:         "+f"{colors[1]}"+elfv+f"{colors[2]}")