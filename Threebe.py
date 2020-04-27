#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Development running command: python3 -B Threebe.py -<OPTION> test_binaies/<FILE_NAME>

# ========== IMPORTS ==========

import sys
import hexdump.hexdump as hexdump
import x86.disassembly as x86disassembly

# ========== FUNCTIONS / CLASSES ==========

def print_help():
    sys.stderr.write("Usage: {0} <parameter(s)> <file(s)>\n".format(sys.argv[0]))
    sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

def print_wrong_file_help():
    sys.stderr.write("ERROR: No such file / Wrong file type.\n")
    sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

# ========== MAIN FUNCTION ==========

def main():
    if len(sys.argv)==1:
        print_help()
    elif len(sys.argv)==3:
        if sys.argv[1]=="-h" or sys.argv[1]=="-H":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexd = file_o.read()

                hexdump.hexdump_parser(hexd)
                file_o.close()
            except:
                print_wrong_file_help()
        elif sys.argv[1]=="-hc" or sys.argv[1]=="-HC":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexd = file_o.read()

                hexdump.hexdump_clean(hexd)
                file_o.close()
            except:
                print_wrong_file_help()
        elif sys.argv[1]=="-hl" or sys.argv[1]=="-HL":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexd = file_o.read()

                print(hexdump.hexdump_clean_for_disassembly(hexd))
                file_o.close()
            except:
                print_wrong_file_help()
        elif sys.argv[1]=="-hw" or sys.argv[1]=="-HW":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexd = file_o.read()

                hexdump.hexdump_clean_without_parsing(hexd)
                file_o.close()
            except:
                print_wrong_file_help()
        elif sys.argv[1]=="-dx86" or sys.argv[1]=="-Dx86" or sys.argv[1]=="-dX86" or sys.argv[1]=="-DX86":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexd = file_o.read()

                hexdfd = hexdump.hexdump_clean_for_disassembly(hexd)
                x86disassembly.disassemble(hexdfd)
                file_o.close()
            except:
                print_wrong_file_help()
        else:
            print_help()
    elif sys.argv[1]=="--help":
        print("{0} - Display a Hexdump / Disassembly of a x86 binary file.".format(sys.argv[0]))
        print("")
        print("Usage:")
        print("{0} <parameter(s)> <file(s)>".format(sys.argv[0]))
        print("")
        print("Possible parameters:")
        print("-h     - Display the hexdump of a given binary file.")
        print("-H     - Display the hexdump of a given binary file.")
        print("-dx86  - Display the disassembly of a given x86 binary file.")
        print("-Dx86  - Display the disassembly of a given x86 binary file.")
        print("-hc    - Display the clean version of the hexdump from a given binary file.")
        print("-HC    - Display the clean version of the hexdump from a given binary file.")
        print("-hl    - Display the clean version of the hexdump from a given binary file as a python list.")
        print("-HL    - Display the clean version of the hexdump from a given binary file as a python list.")
        print("-hw    - Display the clean version of the hexdump from a given binary file without parsing (without grouping / newline characters).")
        print("-HW    - Display the clean version of the hexdump from a given binary file without parsing (without grouping / newline characters).")
        print("--help - Display this help screen.")
        print("")
        print("© Dawid Janikowski 2020-2020")
    else:
        print_help()

# ========== MAIN FUNCTION EXECUTION ==========

if __name__ == "__main__":
    main()