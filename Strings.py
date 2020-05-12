# This file contains funtions that extracts strings from a given (binary) files.

from hexdump.hexdump import bcolors

def extract_binary(ascii):
    streak = 0
    string_toappend = ""
    string_toappend2 = ""
    strings = []
    offset1 = 134512640
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
    print(f"{bcolors.FAIL}- offset - {bcolors.OKGREEN} Length   {bcolors.FAIL}- STRINGS -{bcolors.ENDC}")
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
            print(f"{bcolors.OKBLUE}"+str(offset2)+"  "+f"{bcolors.FAIL}"+after_offset+"     "+f"{bcolors.WARNING}"+i+f"{bcolors.ENDC}")
            prt = True

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