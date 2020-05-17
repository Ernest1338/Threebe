# This file contains functions that parses user input from pathing parameter and are patching given binary.

import sys
from BinArchitecture import bin_architecture

def print_help_address():
    sys.stderr.write("ERROR: Wrong address/offset.\n")
    sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

def print_help_bytes():
    sys.stderr.write("ERROR: Wrong bytes to write.\n")
    sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

def patch_bin(hexdump, address, bytes_to_write, architecture, file_name):
    offset1 = 134512640
    if (len(bytes_to_write)/2)==int(len(bytes_to_write)/2):
        pass
    else:
        print_help_bytes()
        return 1
    if architecture=="x86":
        bytes_pointer = int(address,16) - offset1
        if bytes_pointer<0 or bytes_pointer>len(hexdump):
            print_help_address()
            return 1
    elif architecture=="x86_64":
        bytes_pointer = int(address,16)
    bytes_list = []
    old_bytes = ""
    for i in hexdump:
        bytes_list.append(i)
    for i in range(int(len(bytes_to_write)/2)):
        if len(hex(bytes_list[bytes_pointer])[2:])==1:
            old_bytes += "0"+str(hex(bytes_list[bytes_pointer])[2:])
        else:
            old_bytes += str(hex(bytes_list[bytes_pointer])[2:])
        bytes_list[bytes_pointer]=int(bytes_to_write[i+i:i+i+2],16)
        bytes_pointer+=1
    file_o = open(file_name, 'wb')
    file_o.write(bytes(bytes_list))
    print("Patching succed.")
    print("Old bytes: "+str(''.join(old_bytes)))
    print("New bytes: "+bytes_to_write)

def patch(hexdump, address, bytes_to_write, architecture, file_name):
    if (len(bytes_to_write)/2)==int(len(bytes_to_write)/2):
        pass
    else:
        print_help_bytes()
        return 1
    bytes_pointer = int(address,16)
    bytes_list = []
    old_bytes = ""
    for i in hexdump:
        bytes_list.append(i)
    for i in range(int(len(bytes_to_write)/2)):
        if len(hex(bytes_list[bytes_pointer])[2:])==1:
            old_bytes += "0"+str(hex(bytes_list[bytes_pointer])[2:])
        else:
            old_bytes += str(hex(bytes_list[bytes_pointer])[2:])
        bytes_list[bytes_pointer]=int(bytes_to_write[i+i:i+i+2],16)
        bytes_pointer+=1
    file_o = open(file_name, 'wb')
    file_o.write(bytes(bytes_list))
    print("Patching succed.")
    print("Old bytes: "+str(''.join(old_bytes)))
    print("New bytes: "+bytes_to_write)