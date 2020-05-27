#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Development running command: python3 -B Threebe.py -<OPTION> test_binaies/<FILE_NAME>

# ========== IMPORTS ==========

import sys
import errno
import hexdump.hexdump as hexdump
import x86.disassembly as x86disassembly
import BinInfo as binfo
import Strings as strings
import Patching as patching
from BinArchitecture import bin_architecture

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

        if sys.argv[1]=="-h" or sys.argv[1]=="-H":   # HEXDUMP
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)

                hexdump.hexdump_parser(file_o, bytes_for_hexdump, "@")
            
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-hc" or sys.argv[1]=="-HC":   # HEXDUMP - CLEAN
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                hexdump.hexdump_clean(file_o)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-hs" or sys.argv[1]=="-HS":   # HEXDUMP - SQUASHED
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)

                hexdump.hexdump_parser_compressed(file_o, bytes_for_hexdump, "@")
            
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-h32" or sys.argv[1]=="-H32":   # HEXDUMP - WIDE
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)

                hexdump.hexdump_parser_32(file_o, bytes_for_hexdump, "@")
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-hl" or sys.argv[1]=="-HL":   # HEXDUMP - LIST
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                print(hexdump.hexdump_clean_for_disassembly(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-hw" or sys.argv[1]=="-HW":   # HEXDUMP - WITHOUT PARSING
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                hexdump.hexdump_clean_without_parsing(file_o)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-i" or sys.argv[1]=="-I":   # INFORMATIONS
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                binfo.bin_get_info(hexdump.hexdump_clean_for_disassembly(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sb" or sys.argv[1]=="-SB":   # STRINGS - BINARY
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                strings.extract_binary(hexdump.hexdump_ascii(file_o), hexdump.hexdump_clean_for_disassembly(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sc" or sys.argv[1]=="-SC":   # STRINGS - CLEAN
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                strings.extract_clean(hexdump.hexdump_ascii(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sl" or sys.argv[1]=="-SL":   # STRINGS - LIST
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                strings.extract_list(hexdump.hexdump_ascii(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sw" or sys.argv[1]=="-SW":   # STRINGS - WITHOUT PARSING
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                strings.extract_without_parsing(hexdump.hexdump_ascii(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-s" or sys.argv[1]=="-S":   # STRINGS
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                strings.extract(hexdump.hexdump_ascii(file_o))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-dx86" or sys.argv[1]=="-Dx86" or sys.argv[1]=="-dX86" or sys.argv[1]=="-DX86":   # DISASSEMBLY - x86
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                hexdfd = hexdump.hexdump_clean_for_disassembly(file_o)
                ascii_dict = strings.extract_disassembly(hexdump.hexdump_ascii(file_o), hexdump.hexdump_clean_for_disassembly(file_o))
                x86disassembly.disassemble_x86(hexdfd, ascii_dict)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        else:
            print_help()

    elif len(sys.argv)==5:

        if sys.argv[1]=="-pb" or sys.argv[1]=="-PB": # PATCHING BINARY
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                architecture = bin_architecture(hexdump.hexdump_clean_for_disassembly(file_o))

                patching.patch_bin(file_o, sys.argv[2], sys.argv[3], architecture, file_name)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-p" or sys.argv[1]=="-P": # PATCHING
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                architecture = bin_architecture(hexdump.hexdump_clean_for_disassembly(file_o))

                patching.patch(file_o, sys.argv[2], sys.argv[3], architecture, file_name)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-ha" or sys.argv[1]=="-HA": # HEXDUMP at a given address
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)
                address_to_hexdump = int(sys.argv[2],16)
                bin_arch = bin_architecture(bytes_for_hexdump)
                
                if bin_arch=="x86":
                    if address_to_hexdump>=134512640:
                        offset1 = address_to_hexdump-134512640
                    else:
                        offset1 = address_to_hexdump
                else:
                    offset1 = address_to_hexdump
                file_o2 = []
                for a in range(int(sys.argv[3])):
                    file_o2.append(file_o[a+offset1])

                file_o = bytes(file_o2)
                hexdump.hexdump_parser(file_o, bytes_for_hexdump, address_to_hexdump)
            
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()
            except IndexError as e:
                print_help()

        elif sys.argv[1]=="-h32a" or sys.argv[1]=="-H32A": # HEXDUMP at a given address
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)
                address_to_hexdump = int(sys.argv[2],16)
                bin_arch = bin_architecture(bytes_for_hexdump)
                
                if bin_arch=="x86":
                    if address_to_hexdump>=134512640:
                        offset1 = address_to_hexdump-134512640
                    else:
                        offset1 = address_to_hexdump
                else:
                    offset1 = address_to_hexdump
                file_o2 = []
                for a in range(int(sys.argv[3])):
                    file_o2.append(file_o[a+offset1])

                file_o = bytes(file_o2)
                hexdump.hexdump_parser_32(file_o, bytes_for_hexdump, address_to_hexdump)
            
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()
            except IndexError as e:
                print_help()

    elif sys.argv[1]=="--help":
        print("Threebe - Tool for displaying a Hexdump / Disassembly / Strings / Information from/of a (binary) file.")
        print("")
        print("Usage:")
        print("./Threebe.py <parameter(s)> <file>")
        print("")
        print("Possible parameters:")
        print("-h     - Display the hexdump of a given binary file.")
        print("-h32   - Display the hexdump of a given binary file (32 bytes per line).")
        print("-ha    - Display the hexdump of a given binary file at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
        print("-h32a  - Display the hexdump of a given binary file (32 bytes per line) at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
        print("-hc    - Display the clean version of the hexdump from a given binary file.")
        print("-hl    - Display the hexdump from a given binary file as a python list.")
        print("-hw    - Display the hexdump from a given binary file without parsing (without grouping / newline characters).")
        print('-hs    - Display the hexdump from a given binary file. ("Squashed"/Compressed) version.')
        print("-dx86  - Display the disassembly of a given x86 binary file.")
        print("-i     - Display informations about a given binary file.")
        print("-s     - Display extracted strings from a given file.")
        print("-sb    - Display extracted strings from a given binary file.")
        print("-sc    - Display clean version of extracted strings from a given file.")
        print("-sl    - Display extracted strings from a given file as a python list.")
        print("-sw    - Display extracted strings from a given file without parsing.")
        print("-p     - Patch given binary. Use this option if the binary type you want to patch is not supported. (format the same).")
        print("-pb    - Patch given binary. Format: ./Threebe.py -pb address bytes path/to/binary (address format: 0x0000000, bytes format: 9090).")
        print("--help - Display this help screen.")
        print("")
        print("Original author: Dawid Janikowski 2020-2020")
    else:
        print_help()

# ========== MAIN FUNCTION EXECUTION ==========

if __name__ == "__main__":
    main()