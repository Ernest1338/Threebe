# This file contains funtions that extracts strings from a given (binary) files.

from Hexdump import bcolors
from BinArchitecture import bin_architecture

def extract_binary(ascii, bytes):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    if bin_architecture(bytes)=="x86":
        offset1 = 134512640
    elif bin_architecture(bytes)=="x86_64":
        offset1 = 0
    else:
        offset1 = 0

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(i-len(string_toappend2))
                    strings.append(string_toappend2)
                    
            streak = 0
            string_toappend = ""
            string_toappend2 = ""

    print(f"{bcolors.FAIL}- offset - {bcolors.OKGREEN} Length   {bcolors.FAIL}- string -{bcolors.ENDC}")
    
    prt = True
    for i in strings:
        if prt:
            offset2 = hex(offset1+int(i))
            prt = False
        else:
            if len(str(len(i)))==1:
                after_len = "   "
            elif len(str(len(i)))==2:
                after_len = "  "
            else:
                after_len = " "
            after_offset = " "+str(len(i))+after_len

            offset3 = str(offset2)
            if len(str(offset2))<9:
                for _ in range(9-len(str(offset2))):
                    offset3 = offset3[0:2]+"0"+offset3[2:]

            print(f"{bcolors.OKBLUE}"+offset3+"  "+f"{bcolors.FAIL}"+after_offset+"     "+f"{bcolors.WARNING}"+i+f"{bcolors.ENDC}")
            prt = True

def extract_disassembly(ascii, bytes):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    if bin_architecture(bytes)=="x86":
        offset1 = 134512640
    elif bin_architecture(bytes)=="x86_64":
        offset1 = 0
    else:
        offset1 = 0

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(i-len(string_toappend2))
                    strings.append(string_toappend2)
                    
            streak = 0
            string_toappend = ""
            string_toappend2 = ""

    ascii_dict = {}
    prt = True
    for i in strings:
        if prt:
            offset2 = hex(offset1+int(i))
            prt = False
        else:

            offset3 = str(offset2)
            if len(str(offset2))<9:
                for _ in range(9-len(str(offset2))):
                    offset3 = offset3[0:2]+"0"+offset3[2:]

            ascii_dict[offset3] = i
            prt = True
    return ascii_dict

def extract(ascii):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(i-len(string_toappend2))
                    strings.append(string_toappend2)

            streak = 0
            string_toappend = ""
            string_toappend2 = ""

    print(f"{bcolors.FAIL}Length   - STRINGS -{bcolors.ENDC}")
    prt = True

    for i in strings:
        if prt:
            prt = False
        else:
            if len(str(len(i)))==1:
                after_len = "   "
            elif len(str(len(i)))==2:
                after_len = "  "
            else:
                after_len = " "
            after_offset = str(len(i))+after_len
            print(f"{bcolors.OKBLUE}"+after_offset+"     "+f"{bcolors.WARNING}"+i+f"{bcolors.ENDC}")
            prt = True

def extract_clean(ascii):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(i-len(string_toappend2))
                    strings.append(string_toappend2)

            streak = 0
            string_toappend = ""
            string_toappend2 = ""

    print(f"{bcolors.FAIL}- STRINGS -{bcolors.ENDC}")
    prt = True

    for i in strings:
        if prt:
            prt = False
        else:
            print(f"{bcolors.WARNING}"+i+f"{bcolors.ENDC}")
            prt = True

def extract_list(ascii):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(string_toappend2)

            streak = 0
            string_toappend = ""
            string_toappend2 = ""

    print(strings)

def extract_without_parsing(ascii):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []

    for i in range(len(ascii)):
        if ascii[i] != False:
            streak += 1
            string_toappend += ascii[i]
        else:
            if streak>2:
                for a in string_toappend:
                    if ord(a)>=32 and ord(a)<=126:
                        string_toappend2 += a
                    else:
                        pass

                if len(string_toappend2)<=2:
                    pass
                else:
                    strings.append(i-len(string_toappend2))
                    strings.append(string_toappend2)

            streak = 0
            string_toappend = ""
            string_toappend2 = ""
    prt = True

    for i in strings:
        if prt:
            prt = False
        else:
            print(i)
            prt = True