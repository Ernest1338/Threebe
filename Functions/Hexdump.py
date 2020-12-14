# This is an file containing different functions that parses binary data in a variety of ways.

from Functions.BinArchitecture import bin_architecture

def hexdump_clean_for_disassembly(hexdump):
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    for i in parsed2:
        if len(i)==2:
            parsed3 += str(i)+" "
        else:
            parsed3 += str(hex(ord(i))[2:])+" "
    return parsed3[:-1].upper().split(" ")

def hexdump_clean(hexdump):
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    for i in parsed2:
        if len(parsed3)<48:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            print(parsed3.upper()) #len - 51
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "

    for i in range(51-len(parsed3)):
        parsed3 += " "
    print(parsed3.upper())
    return True

def hexdump_parser_32(hexdump, bytes, address1, colors):
    bcolors = colors
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    if address1 == "@":
        if bin_architecture(bytes)=="x86":
            offset1 = 134512640
        elif bin_architecture(bytes)=="x86_64":
            offset1 = 0
        else:
            offset1 = 0
    else:
        offset1 = address1

    print(f"{bcolors.FAIL}- offset -{bcolors.OKBLUE}  A  B  C  D   E  F  G  H   I  J  K  L   M  N  O  P   Q  R  S  T   U  V  W  X   Y  Z  0  1   2  3  4  5  {bcolors.FAIL}- ASCII -{bcolors.RESET}")

    for i in parsed2:
        if len(parsed3)<96:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            ascii1 = ""
            parsed4 = "" # colored version of the hex view (old)
            parsed5 = []
            for a in parsed3.split(" "):
                try:
                    if chr(int(a,16)).isprintable():
                        ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                        parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                        parsed5.append(True)
                    else:
                        ascii1 += "."
                        parsed4 += str(a)+" "
                        parsed5.append(False)
                except:
                    pass
            parsed6 = parsed3[:-1].split(" ")
            for b in range(len(parsed6)):
                try:
                    if parsed5[b] == True:
                        parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"+" "
                    else:
                        parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
                except:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
            parsed6.insert(4, " ")
            parsed6.insert(9, " ")
            parsed6.insert(14, " ")
            parsed6.insert(19, " ")
            parsed6.insert(24, " ")
            parsed6.insert(29, " ")
            parsed6.insert(34, " ")
            parsed7 = "".join(parsed6)

            offset2 = str(hex(offset1))
            if len(str(hex(offset1)))<9:
                for _ in range(9-len(str(hex(offset1)))):
                    offset2 = offset2[0:2]+"0"+offset2[2:]
            print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET}  "+parsed7+f"{bcolors.OKBLUE}| {bcolors.RESET}"+ascii1) #len - 51

            offset1 += 32
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "

    ascii1 = ""
    parsed4 = "" # colored version of the hex view (old)
    parsed5 = []
    for a in parsed3.split(" "):
        try:
            if chr(int(a,16)).isprintable():
                ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                parsed5.append(True)
            else:
                ascii1 += "."
                parsed4 += str(a)+" "
                parsed5.append(False)
        except:
            pass
    try:
        parsed6 = parsed3[:-1].split(" ")
        for b in range(len(parsed6)):
            try:
                if parsed5[b] == True:
                    parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"+" "
                else:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
            except:
                parsed6[b] = str(parsed3.split(" ")[b].upper())+" "

        parsed6.insert(4, " ")
        parsed6.insert(9, " ")
        parsed6.insert(14, " ")
        parsed6.insert(19, " ")
        parsed6.insert(24, " ")
        parsed6.insert(29, " ")
        parsed6.insert(34, " ")
        parsed7 = "".join(parsed6)
    except:
        pass

    for i in range(99-(len(parsed3)+3)):
        parsed7 += " "

    offset2 = str(hex(offset1))
    if len(str(hex(offset1)))<9:
        for _ in range(9-len(str(hex(offset1)))):
            offset2 = offset2[0:2]+"0"+offset2[2:]

    print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET}  "+parsed7+f"{bcolors.OKBLUE}| {bcolors.RESET}"+ascii1)

    return True

def hexdump_ascii(hexdump, colors):
    bcolors = colors
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    _ascii = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    offset1 = 134512640

    for i in parsed2:
        if len(parsed3)<48:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            ascii1 = ""
            parsed4 = "" # colored version of the hex view (old)
            parsed5 = []
            for a in parsed3.split(" "):
                try:
                    if chr(int(a,16)).isprintable():
                        ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                        _ascii.append(chr(int(a,16)))
                        parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                        parsed5.append(True)
                    else:
                        ascii1 += "."
                        _ascii.append(False)
                        parsed4 += str(a)+" "
                        parsed5.append(False)
                except:
                    pass
            parsed6 = parsed3[:-1].split(" ")
            parsed6.insert(4, " ")
            parsed6.insert(9, " ")
            parsed6.insert(14, " ")
            parsed7 = "".join(parsed6)

            offset1 += 16
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "

    ascii1 = ""
    parsed4 = "" # colored version of the hex view (old)
    parsed5 = []
    for a in parsed3.split(" "):
        try:
            if chr(int(a,16)).isprintable():
                ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                _ascii.append(chr(int(a,16)))
                parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                parsed5.append(True)
            else:
                ascii1 += "."
                _ascii.append(False)
                parsed4 += str(a)+" "
                parsed5.append(False)
        except:
            pass
    try:
        parsed6 = parsed3[:-1].split(" ")
        for b in range(len(parsed6)):
            if parsed5[b] == True:
                parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"+" "
            else:
                parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
        parsed6.insert(4, " ")
        parsed6.insert(9, " ")
        parsed6.insert(14, " ")
        parsed7 = "".join(parsed6)
    except:
        pass

    for i in range(51-(len(parsed3)+3)):
        parsed7 += " "

    return _ascii

def hexdump_parser(hexdump, bytes, address1, colors):
    bcolors = colors
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    if address1 == "@":
        if bin_architecture(bytes)=="x86":
            offset1 = 134512640
        elif bin_architecture(bytes)=="x86_64":
            offset1 = 0
        else:
            offset1 = 0
    else:
        offset1 = address1

    print(f"{bcolors.FAIL}- offset -{bcolors.OKBLUE}  A  B  C  D   E  F  G  H   I  J  K  L   M  N  O  P  {bcolors.FAIL}- ASCII -{bcolors.RESET}")

    for i in parsed2:
        if len(parsed3)<48:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            ascii1 = ""
            parsed4 = "" # colored version of the hex view (old)
            parsed5 = []
            for a in parsed3.split(" "):
                try:
                    if chr(int(a,16)).isprintable():
                        ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                        parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                        parsed5.append(True)
                    else:
                        ascii1 += "."
                        parsed4 += str(a)+" "
                        parsed5.append(False)
                except:
                    pass
            parsed6 = parsed3[:-1].split(" ")
            for b in range(len(parsed6)):
                try:
                    if parsed5[b] == True:
                        parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"+" "
                    else:
                        parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
                except:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())+" "

            parsed6.insert(4, " ")
            parsed6.insert(9, " ")
            parsed6.insert(14, " ")
            parsed7 = "".join(parsed6)

            offset2 = str(hex(offset1))
            if len(str(hex(offset1)))<9:
                for _ in range(9-len(str(hex(offset1)))):
                    offset2 = offset2[0:2]+"0"+offset2[2:]

            print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET}  "+parsed7+f"{bcolors.OKBLUE}| {bcolors.RESET}"+ascii1) #len - 51

            offset1 += 16
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "

    ascii1 = ""
    parsed4 = "" # colored version of the hex view (old)
    parsed5 = []
    for a in parsed3.split(" "):
        try:
            if chr(int(a,16)).isprintable():
                ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                parsed5.append(True)
            else:
                ascii1 += "."
                parsed4 += str(a)+" "
                parsed5.append(False)
        except:
            pass
    try:
        parsed6 = parsed3[:-1].split(" ")
        for b in range(len(parsed6)):
            try:
                if parsed5[b] == True:
                    parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"+" "
                else:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
            except:
                parsed6[b] = str(parsed3.split(" ")[b].upper())+" "
        parsed6.insert(4, " ")
        parsed6.insert(9, " ")
        parsed6.insert(14, " ")
        parsed7 = "".join(parsed6)
    except:
        pass

    for i in range(51-(len(parsed3)+3)):
        parsed7 += " "

    offset2 = str(hex(offset1))
    if len(str(hex(offset1)))<9:
        for _ in range(9-len(str(hex(offset1)))):
            offset2 = offset2[0:2]+"0"+offset2[2:]
            
    print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET}  "+parsed7+f"{bcolors.OKBLUE}| {bcolors.RESET}"+ascii1)

    return True

def hexdump_parser_compressed(hexdump, bytes, address1, colors):
    bcolors = colors
    hexdump = str(hexdump)
    parsed1 = hexdump[2:-1]
    parsed2 = []
    flag1 = False
    flag2 = False
    flag3 = False

    for i in range(len(parsed1)):
        if parsed1[i]=="\\":
            flag1 = True
            if parsed1[i+1]=="\\":
                parsed2.append(parsed1[i])
        elif flag1:
            flag1 = False
            flag2 = True

            if parsed1[i]!="x":
                if parsed1[i]=="t":
                    parsed2.append("09")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="n":
                    parsed2.append("0A")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                elif parsed1[i]=="r":
                    parsed2.append("0D")
                    flag1 = False
                    flag2 = False
                    flag3 = False
                else:
                    parsed2.append(parsed1[i])
                    flag1 = False
                    flag2 = False
                    flag3 = False
        elif flag2:
            flag2 = False
            flag3 = True
        elif flag3:
            parsed2.append(parsed1[i-1]+parsed1[i])
            flag3 = False
        else:
            parsed2.append(parsed1[i])

    parsed3 = ""
    if address1 == "@":
        if bin_architecture(bytes)=="x86":
            offset1 = 134512640
        elif bin_architecture(bytes)=="x86_64":
            offset1 = 0
        else:
            offset1 = 0
    else:
        offset1 = address1

    print(f"{bcolors.FAIL}- offset -{bcolors.OKBLUE} A B C D  E F G H  I J K L  M N O P  {bcolors.FAIL}- ASCII -{bcolors.RESET}")

    for i in parsed2:
        if len(parsed3)<48:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            ascii1 = ""
            parsed4 = "" # colored version of the hex view (old)
            parsed5 = []
            for a in parsed3.split(" "):
                try:
                    if chr(int(a,16)).isprintable():
                        ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                        parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                        parsed5.append(True)
                    else:
                        ascii1 += "."
                        parsed4 += str(a)+" "
                        parsed5.append(False)
                except:
                    pass
            parsed6 = parsed3[:-1].split(" ")
            for b in range(len(parsed6)):
                try:
                    if parsed5[b] == True:
                        parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"
                    else:
                        parsed6[b] = str(parsed3.split(" ")[b].upper())
                except:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())

            parsed6.insert(4, " ")
            parsed6.insert(9, " ")
            parsed6.insert(14, " ")
            parsed7 = "".join(parsed6)

            offset2 = str(hex(offset1))
            if len(str(hex(offset1)))<9:
                for _ in range(9-len(str(hex(offset1)))):
                    offset2 = offset2[0:2]+"0"+offset2[2:]

            print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET} "+parsed7+f"{bcolors.OKBLUE} |{bcolors.RESET}"+ascii1) #len - 51

            offset1 += 16
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "

    ascii1 = ""
    parsed4 = "" # colored version of the hex view (old)
    parsed5 = []
    for a in parsed3.split(" "):
        try:
            if chr(int(a,16)).isprintable():
                ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.RESET}"
                parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.RESET}"+" "
                parsed5.append(True)
            else:
                ascii1 += "."
                parsed4 += str(a)+" "
                parsed5.append(False)
        except:
            pass
    try:
        parsed6 = parsed3[:-1].split(" ")
        for b in range(len(parsed6)):
            try:
                if parsed5[b] == True:
                    parsed6[b] = f"{bcolors.WARNING}"+str(parsed3.split(" ")[b].upper())+f"{bcolors.RESET}"
                else:
                    parsed6[b] = str(parsed3.split(" ")[b].upper())
            except:
                parsed6[b] = str(parsed3.split(" ")[b].upper())
        parsed6.insert(4, " ")
        parsed6.insert(9, " ")
        parsed6.insert(14, " ")
        parsed7 = "".join(parsed6)
    except:
        pass

    for i in range(39-(len(parsed3)+3)):
        parsed7 += " "

    offset2 = str(hex(offset1))
    if len(str(hex(offset1)))<9:
        for _ in range(9-len(str(hex(offset1)))):
            offset2 = offset2[0:2]+"0"+offset2[2:]
            
    print(f"{bcolors.OKBLUE}"+offset2+f"{bcolors.RESET} "+parsed7+f"{bcolors.OKBLUE} |{bcolors.RESET}"+ascii1)

    return True