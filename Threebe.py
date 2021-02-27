#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Development running command: python3 -B Threebe.py -<OPTION> test_binaies/<FILE_NAME>

# ========== IMPORTS ==========

import sys
import errno
import Functions.Hexdump as hexdump
import Architectures.x86.x86disassembly as x86disassembly
import Functions.BinInfo as binfo
import Functions.Strings as strings
import Functions.Patching as patching
from Functions.BinArchitecture import bin_architecture
from Functions.Colors import returnColors

# ========== FUNCTIONS / CLASSES ==========

def print_help():
    bcolors = returnColors(1)
    sys.stderr.write(f"{bcolors.FAIL}Usage: {sys.argv[0]} <parameter(s)> <file(s)>\n")
    sys.stderr.write(f"For help use the --help parameter: {sys.argv[0]} --help{bcolors.RESET}\n")

def print_wrong_file_help():
    bcolors = returnColors(1)
    sys.stderr.write(f"{bcolors.FAIL}ERROR: No such file / Wrong file type.\n")
    sys.stderr.write(f"For help use the --help parameter: {sys.argv[0]} --help{bcolors.RESET}\n")

def print_usage(clean):
    if clean:
        helpColors = ['','','','']
    else:
        bcolors = returnColors(1)
        helpColors = [bcolors.WARNING, bcolors.OKGREEN, bcolors.OKBLUE, bcolors.RESET]
    print(f"{helpColors[0]}Threebe {helpColors[2]}- Tool for displaying a Hexdump / Disassembly / Strings / Information from/of a (binary) file.")
    print("")
    print("Usage:")
    print(f"{helpColors[1]}./{sys.argv[0]} <parameter(s)> <file>")
    print(f"{helpColors[2]}")
    print(f"{helpColors[0]}Possible parameters:")
    print(f"{helpColors[2]}")
    print("===== HEXDUMP =====")
    print(f"{helpColors[1]}")
    print("-h     - Display the hexdump of a given (binary) file.")
    print("-h32   - Display the hexdump of a given (binary) file (32 bytes per line).")
    print("-ha    - Display the hexdump of a given (binary) file at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
    print("-h32a  - Display the hexdump of a given (binary) file (32 bytes per line) at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
    print("-hc    - Display the clean version of the hexdump from a given (binary) file.")
    print("-hl    - Display the hexdump from a given (binary) file as a python list.")
    print("-hw    - Display the hexdump from a given (binary) file without parsing (without ascii and offsets).")
    print('-hs    - Display the hexdump from a given (binary) file. ("Squashed"/Compressed) version.')
    print("")
    print(f"{helpColors[2]}===== DISASSEMBLY =====")
    print(f"{helpColors[1]}")
    print("-dx86  - Display the disassembly of a given x86 binary file.")
    print("")
    print(f"{helpColors[2]}===== INFORMATION =====")
    print(f"{helpColors[1]}")
    print("-i     - Display informations about a given binary file.")
    print("-ic    - Display clean version (without colors) of informations about a given binary file.")
    print("")
    print(f"{helpColors[2]}===== STRINGS =====")
    print(f"{helpColors[1]}")
    print("-s     - Display extracted strings from a given file.")
    print("-sb    - Display extracted strings from a given binary file.")
    print("-sc    - Display clean version of extracted strings from a given file.")
    print("-sl    - Display extracted strings from a given file as a python list.")
    print("-sw    - Display extracted strings from a given file without parsing.")
    print(f"{helpColors[2]}")
    print("===== PATCHING =====")
    print(f"{helpColors[1]}")
    print("-pb    - Patch given binary. Format: ./Threebe.py -pb address bytes path/to/binary (address format: 0x0000000, bytes format: 9090).")
    print("-pbc   - Patch given binary. Clean version (without colors). Format is the same.")
    print("-p     - Patch given binary. Use this option if the binary type you want to patch is not supported. (format the same)")
    print("-pc    - Patch given binary. Clean version. Use this option if the binary type you want to patch is not supported. (format the same)")
    print(f"{helpColors[2]}")
    print("===== OTHERS =====")
    print(f"{helpColors[1]}")
    print("--help - Display help screen.")
    print("--help-clean - Display help screen without any coloring.")
    print("--help-simple - Display simple version of help screen.")
    print("--help-simple-clean - Display simple version of help screen without any coloring.")
    print(f"{helpColors[2]}")
    print(f"Original author: Dawid J. (Ernest Gupik) 2020-2021{helpColors[3]}")

def print_usage_simple(clean):
    if clean:
        helpColors = ['','','','']
    else:
        bcolors = returnColors(1)
        helpColors = [bcolors.WARNING, bcolors.OKGREEN, bcolors.OKBLUE, bcolors.RESET]
    print(f"{helpColors[2]}Usage:")
    print(f"{helpColors[1]}./{sys.argv[0]} <parameter(s)> <file>")
    print(f"{helpColors[2]}")
    print(f"{helpColors[0]}Possible parameters:{helpColors[1]}")
    print("-h     - Display the hexdump of a given (binary) file.")
    print("-h32   - Display the hexdump of a given (binary) file (32 bytes per line).")
    print("-ha    - Display the hexdump of a given (binary) file at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
    print("-h32a  - Display the hexdump of a given (binary) file (32 bytes per line) at given address. Format: ./Threebe.py -ha 0xADDRESS HOW_MUCH path/to/binary")
    print("-hc    - Display the clean version of the hexdump from a given (binary) file.")
    print("-hl    - Display the hexdump from a given (binary) file as a python list.")
    print("-hw    - Display the hexdump from a given (binary) file without parsing (without ascii and offsets).")
    print('-hs    - Display the hexdump from a given (binary) file. ("Squashed"/Compressed) version.')
    print("-dx86  - Display the disassembly of a given x86 binary file.")
    print("-i     - Display informations about a given binary file.")
    print("-ic    - Display clean version (without colors) of informations about a given binary file.")
    print("-s     - Display extracted strings from a given file.")
    print("-sb    - Display extracted strings from a given binary file.")
    print("-sc    - Display clean version of extracted strings from a given file.")
    print("-sl    - Display extracted strings from a given file as a python list.")
    print("-sw    - Display extracted strings from a given file without parsing.")
    print("-pb    - Patch given binary. Format: ./Threebe.py -pb address bytes path/to/binary (address format: 0x0000000, bytes format: 9090).")
    print("-pbc   - Patch given binary. Clean version (without colors). Format is the same.")
    print("-p     - Patch given binary. Use this option if the binary type you want to patch is not supported. (format the same)")
    print("-pc    - Patch given binary. Clean version. Use this option if the binary type you want to patch is not supported. (format the same)")
    print("--help - Display help screen.")
    print("--help-clean - Display help screen without any coloring.")
    print("--help-simple - Display simple version of help screen.")
    print("--help-simple-clean - Display simple version of help screen without any coloring.")

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

                bcolors = returnColors(1)
                hexdump.hexdump_parser(file_o, bytes_for_hexdump, "@", bcolors)

            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-hc" or sys.argv[1]=="-HC":   # HEXDUMP - CLEAN
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()
                bytes_for_hexdump = hexdump.hexdump_clean_for_disassembly(file_o)

                bcolors = returnColors(2)
                hexdump.hexdump_parser(file_o, bytes_for_hexdump, "@", bcolors)

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

                bcolors = returnColors(1)
                hexdump.hexdump_parser_compressed(file_o, bytes_for_hexdump, "@", bcolors)

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
                bcolors = returnColors(1)
                hexdump.hexdump_parser_32(file_o, bytes_for_hexdump, "@", bcolors)
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

                hexdump.hexdump_clean(file_o)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-i" or sys.argv[1]=="-I":   # INFORMATIONS
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                binfo.bin_get_info(hexdump.hexdump_clean_for_disassembly(file_o), bcolors)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-ic" or sys.argv[1]=="-IC":   # INFORMATIONS - CLEAN
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(2)
                binfo.bin_get_info(hexdump.hexdump_clean_for_disassembly(file_o), bcolors)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sb" or sys.argv[1]=="-SB":   # STRINGS - BINARY
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                strings.extract_binary(hexdump.hexdump_ascii(file_o, bcolors), hexdump.hexdump_clean_for_disassembly(file_o), bcolors)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sc" or sys.argv[1]=="-SC":   # STRINGS - CLEAN
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                strings.extract_clean(hexdump.hexdump_ascii(file_o, bcolors), bcolors, True)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sl" or sys.argv[1]=="-SL":   # STRINGS - LIST
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                strings.extract_list(hexdump.hexdump_ascii(file_o, bcolors))
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-sw" or sys.argv[1]=="-SW":   # STRINGS - WITHOUT PARSING
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(2)
                strings.extract_clean(hexdump.hexdump_ascii(file_o, bcolors), bcolors, False)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-s" or sys.argv[1]=="-S":   # STRINGS
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                strings.extract(hexdump.hexdump_ascii(file_o, bcolors), bcolors)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-dx86" or sys.argv[1]=="-Dx86" or sys.argv[1]=="-dX86" or sys.argv[1]=="-DX86":   # DISASSEMBLY - x86
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb').read()

                bcolors = returnColors(1)
                hexdfd = hexdump.hexdump_clean_for_disassembly(file_o)
                ascii_dict = strings.extract_disassembly(hexdump.hexdump_ascii(file_o, bcolors), hexdump.hexdump_clean_for_disassembly(file_o))
                x86disassembly.disassemble_x86(hexdfd, ascii_dict, bcolors)
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
                bcolors = returnColors(1)
                if architecture != 1:
                    patching.patch_bin(file_o, sys.argv[2], sys.argv[3], architecture, file_name, bcolors)
                else:
                    sys.stderr.write(f"{bcolors.FAIL}ERROR: File header not recognized.\n")
                    sys.stderr.write("This may be because this binary type is not yet supported or your binary's header got corrupted.\n")
                    sys.stderr.write(f"Try using -p function. (Remember to change addresses in that case.){bcolors.RESET}\n")
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()
        
        elif sys.argv[1]=="-pbc" or sys.argv[1]=="-PBC": # PATCHING BINARY -  CLEAN
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                architecture = bin_architecture(hexdump.hexdump_clean_for_disassembly(file_o))
                bcolors = returnColors(2)
                if architecture != 1:
                    patching.patch_bin(file_o, sys.argv[2], sys.argv[3], architecture, file_name, bcolors)
                else:
                    sys.stderr.write(f"{bcolors.FAIL}ERROR: File header not recognized.\n")
                    sys.stderr.write("This may be because this binary type is not yet supported or your binary's header got corrupted.\n")
                    sys.stderr.write(f"Try using -p function. (Remember to change addresses in that case.){bcolors.RESET}\n")
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

                bcolors = returnColors(1)
                patching.patch(file_o, sys.argv[2], sys.argv[3], architecture, file_name, bcolors)
            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()

        elif sys.argv[1]=="-pc" or sys.argv[1]=="-PC": # PATCHING - CLEAN
            try:
                file_name = sys.argv[4]
                file_o = open(file_name,'rb').read()
                architecture = bin_architecture(hexdump.hexdump_clean_for_disassembly(file_o))

                bcolors = returnColors(2)
                patching.patch(file_o, sys.argv[2], sys.argv[3], architecture, file_name, bcolors)
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
                bcolors = returnColors(1)
                hexdump.hexdump_parser(file_o, bytes_for_hexdump, address_to_hexdump, bcolors)

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
                bcolors = returnColors(1)
                hexdump.hexdump_parser_32(file_o, bytes_for_hexdump, address_to_hexdump, bcolors)

            except IOError as e:
                if e.errno == errno.EPIPE:
                    pass
                else:
                    print_wrong_file_help()
            except IndexError as e:
                print_help()
        else:
            print_help()

    elif sys.argv[1]=="--help":
        print_usage(False)
    elif sys.argv[1]=="--help-clean":
        print_usage(True)
    elif sys.argv[1]=="--help-simple":
        print_usage_simple(False)
    elif sys.argv[1]=="--help-simple-clean":
        print_usage_simple(True)
    else:
        print_help()

# ========== MAIN FUNCTION EXECUTION ==========

if __name__ == "__main__":
    main()