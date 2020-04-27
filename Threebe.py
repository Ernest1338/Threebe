#!/usr/bin/python
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    print(parsed3[:-1].upper().split(" "))
    return True

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

def hexdump_parser(hexdump):
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
    offset1 = 2152202240
    print(f"{bcolors.FAIL}- offset -{bcolors.OKBLUE}   A  B  C  D   E  F  G  H   I  J  K  L   M  N  O  P  {bcolors.FAIL}- ASCII -{bcolors.ENDC}")
    for i in parsed2:
        if len(parsed3)<48:
            if len(i)==2:
                parsed3 += str(i)+" "
            else:
                parsed3 += str(hex(ord(i))[2:])+" "
        else:
            ascii1 = ""
            parsed4 = ""
            for a in parsed3.split(" "):
                try:
                    if chr(int(a,16)).isprintable():
                        ascii1 += f"{bcolors.WARNING}"+chr(int(a,16))+f"{bcolors.ENDC}"
                        parsed4 += f"{bcolors.WARNING}"+str(a)+f"{bcolors.ENDC}"+" "
                    else:
                        ascii1 += "."
                        parsed4 += str(a)+" "
                except:
                    pass
            parsed3 = parsed3[:12]+""+parsed3[11:24]+" "+parsed3[24:36]+" "+parsed3[36:]
            print(f"{bcolors.OKBLUE}"+str(hex(offset1))+f"{bcolors.ENDC}  "+parsed3.upper()+f"{bcolors.OKBLUE}| {bcolors.ENDC}"+ascii1) #len - 51
            offset1 += 16
            if len(i)==2:
                parsed3 = str(i)+" "
            else:
                parsed3 = str(hex(ord(i))[2:])+" "
    ascii1 = ""
    for a in parsed3.split(" "):
        try:
            if chr(int(a,16)).isprintable():
                ascii1 += chr(int(a,16))
            else:
                ascii1 += "."
        except:
            pass
    try:
        parsed3 = parsed3[:12]+""+parsed3[11:24]+" "+parsed3[24:36]+" "+parsed3[36:]
    except:
        pass
    for i in range(51-len(parsed3)):
        parsed3 += " "
    print(f"{bcolors.OKBLUE}"+str(hex(offset1))+f"{bcolors.ENDC}  "+parsed3.upper()+f"{bcolors.OKBLUE}| {bcolors.ENDC}"+ascii1)
    return True

def main():
    if len(sys.argv)==1:
        sys.stderr.write("Usage: {0} <parameter(s)> <file(s)>\n".format(sys.argv[0]))
        sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))
    elif len(sys.argv)==3:
        if sys.argv[1]=="-h" or sys.argv[1]=="-H":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexdump = file_o.read()

                hexdump_parser(hexdump)
                file_o.close()
            except:
                sys.stderr.write("ERROR: No such file / Wrong file type.\n")
                sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))
        elif sys.argv[1]=="-hc" or sys.argv[1]=="-HC":
            try:
                file_name = sys.argv[2]
                file_o = open(file_name,'rb')
                hexdump = file_o.read()

                hexdump_clean_for_disassembly(hexdump)
                file_o.close()
            except:
                sys.stderr.write("ERROR: No such file / Wrong file type.\n")
                sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))
        elif sys.argv[1]=="-d" or sys.argv[1]=="-D":
            pass
        else:
            sys.stderr.write("Usage: {0} <parameter(s)> <file(s)>\n".format(sys.argv[0]))
            sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))
    elif sys.argv[1]=="--help":
        print("{0} - Display a Hexdump / Disassembly of a x86 binary file.".format(sys.argv[0]))
        print("")
        print("Usage:")
        print("{0} <parameter(s)> <file(s)>".format(sys.argv[0]))
        print("")
        print("Possible parameters:")
        print("-h     - Display the hexdump of a given binary file.")
        print("-H     - Display the hexdump of a given binary file.")
        print("-hc     - Display the clean version of the hexdump from a given binary file.")
        print("-HC     - Display the clean version of the hexdump from a given binary file.")
        print("--help - Display the help screen.")
        print("")
        print("© Dawid Janikowski 2020")
    else:
        sys.stderr.write("Usage: {0} <parameter(s)> <file(s)>\n".format(sys.argv[0]))
        sys.stderr.write("For help use the --help parameter: {0} --help\n".format(sys.argv[0]))

if __name__ == "__main__":
    main()