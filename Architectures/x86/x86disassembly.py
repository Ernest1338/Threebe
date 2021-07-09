# This file contains function(s) that translates raw bytes into assembly instructions using x86opcodesTable and some python logic.

import Architectures.x86.x86opcodesTable as x86opT

times = 0

def cancle_function_iteration(howmany):
    global times
    times += int(howmany)

def disassemble_x86(bytes, ascii_dict, colors):
    global times
    bcolors = colors
    if bcolors.HEADER == '':
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            BOLD = '\033[01m'
            UNDERLINE = '\033[04m'
            RESET = '\033[00m'
        isClean = True
    else:
        isClean = False
    offset1 = 134512640
    counter1 = 0

    for i in bytes:

        if isClean:
            class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                BOLD = '\033[01m'
                UNDERLINE = '\033[04m'
                RESET = '\033[00m'

        if times == 0:
            to_display = i
            after_instruction = ""
            after_byte = ""

            if i in x86opT.x86opcodes:
                instruction = x86opT.x86opcodes[i]
                intruction_len_for_check = 51+len(instruction) # need to add to this after_instruction every time this variable (after_instruction) is usesd inside an if
                should_print = True

                if i == "74" or i == "75" or i == "7E" or i == "7F" or i == "70" or i == "71" or i == "72" or i == "73": # JE, JNE, JLE, JG, JO, JNO, JB, JAE
                    after_byte = " "+bytes[counter1+1]
                    if int(bytes[counter1+1],16)>=128:
                        if int(bytes[counter1+1],16)==255:
                            after_instruction = " "+hex(offset1+1)
                        elif int(bytes[counter1+1],16)==254:
                            after_instruction = " "+hex(offset1)
                        else:
                            after_instruction = " "+hex(offset1-(256-(int(bytes[counter1+1],16)+2)))
                    else:
                        after_instruction = " "+hex(offset1+(int(bytes[counter1+1],16)+2))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                # 1 byte instructions
                elif  (i == "90" or i == "55" or i == "50" or i == "56" or i == "57" or i == "51" or i == "53" or i == "52" or i == "54" or i == "0E" or i == "16" or i == "1E" or i == "06"
                    or i == "1F" or i == "07" or i == "17" or i == "58" or i == "59" or i == "5A" or i == "5B" or i == "5C" or i == "5D" or i == "5E" or i == "5F" or i == "61" or i == "4C" or i == "49"
                    or i == "4E" or i == "4F" or i == "48" or i == "46" or i == "44" or i == "47" or i == "42" or i == "43" or i == "40" or i == "41" or i == "C9" or i == "C3" or i == "27" or i == "2F"
                    or i == "CF" or i == "98" or i == "99" or i == "4A" or i == "4B" or i == "4D" or i == "45"):
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""

                elif i == "01": # ADD
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="CA":
                        after_instruction = " edx, ecx"
                    elif bytes[counter1+1]=="D0":
                        after_instruction = " eax, edx"
                    elif bytes[counter1+1]=="01":
                        after_instruction = " dword [ecx], eax"
                    elif bytes[counter1+1]=="00":
                        after_instruction = " dword [eax], eax"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "BA": # MOV edx, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = ", "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "89": # MOV ebp, esp; MOV ebx, ecx
                    after_byte = " "+bytes[counter1+1]
                    _89var = bytes[counter1+1]
                    if _89var=="E5":
                        after_instruction = " ebp, esp"
                    if _89var=="CB":
                        after_instruction = " ebx, ecx"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "8B": # MOV
                    after_byte = " "+bytes[counter1+1]
                    _8Bvar = 1
                    if bytes[counter1+1]=="1C":
                        if bytes[counter1+2]=="24":
                            after_instruction = " ebx, dword [esp]"
                            after_byte += " "+bytes[counter1+2]
                            _8Bvar += 1
                    elif bytes[counter1+1]=="10":
                        after_instruction = " edx, dword [eax]"
                    elif bytes[counter1+1]=="55":
                        after_instruction = " edx, dword [var_4h]"
                    elif bytes[counter1+1]=="45":
                        after_instruction = " eax, dword [arg_8h]"
                    elif bytes[counter1+1]=="4D":
                        after_instruction = " ecx, dword [var_4h]"
                    elif bytes[counter1+1]=="00":
                        after_instruction = " eax, dword [eax]"
                    elif bytes[counter1+1]=="6C":
                        after_instruction = " ebp, dword [arg_4h]"
                    elif bytes[counter1+1]=="43":
                        _8Bvar2 = str(bytes[counter1+2])
                        if str(bytes[counter1+2][0])=="0":
                            _8Bvar2 = str(bytes[counter1+2][1])
                        after_instruction = " eax, dword [ebx + "+str(_8Bvar2)+"]"
                        _8Bvar = 2
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(_8Bvar)

                elif i == "83": # ADD, CMP, SUB, OR
                    after_byte = " "+bytes[counter1+1]+" "+bytes[counter1+2]
                    ADD83var = bytes[counter1+2]
                    ADD83var2 = 2
                    ADD83var3 = bytes[counter1+3]
                    ADD83var4 = str(int(ADD83var,16))
                    if bytes[counter1+2][0]=="0":
                        ADD83var = bytes[counter1+2][1]
                    if bytes[counter1+3][0]=="0":
                        ADD83var3 = bytes[counter1+3][1]
                    if bytes[counter1+1]=="C2":
                        after_instruction = " edx, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="C4":
                        after_instruction = " esp, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="C7":
                        after_instruction = " edi, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="C0":
                        after_instruction = " eax, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="F8":
                        instruction = "CMP"
                        after_instruction = " eax, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="3B":
                        instruction = "CMP"
                        after_instruction = " dword [ebx], "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="EC":
                        instruction = "SUB"
                        after_instruction = " esp, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="EA":
                        instruction = "SUB"
                        after_instruction = " edx, "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="08":
                        instruction = "OR"
                        if ADD83var=="FF":
                            ADD83var4 = "-1"
                        after_instruction = " dword [eax], "+"0x"+str(ADD83var.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                    elif bytes[counter1+1]=="E4":
                        instruction = "AND"
                        if ADD83var=="FF":
                            ADD83var4 = "-1"
                        elif ADD83var[0]=="F":
                            ADD83var = "FFFFFF"+ADD83var
                        after_instruction = " esp, "+"0x"+str(ADD83var.lower())
                    elif bytes[counter1+1]=="45" and bytes[counter1+2]=="FC":
                        ADD83var4 = str(int(bytes[counter1+3],16))
                        after_instruction = " dword [var_4h], "+"0x"+str(ADD83var3.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                        after_byte += " "+bytes[counter1+3]
                        ADD83var2 = 4
                    elif bytes[counter1+1]=="7D" and bytes[counter1+2]=="08":
                        ADD83var4 = str(int(bytes[counter1+3],16))
                        instruction = "CMP"
                        after_instruction = " dword [arg_8h], "+"0x"+str(ADD83var3.lower())
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+ADD83var4
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+ADD83var4
                        after_byte += " "+bytes[counter1+3]
                        ADD83var2 = 4
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(ADD83var2)

                elif i == "68": # PUSH string
                    after_byte = " "+bytes[counter1+1]+" "+bytes[counter1+2]+" "+bytes[counter1+3]+" "+bytes[counter1+4]
                    _68offset = " 0x"+bytes[counter1+4]+bytes[counter1+3]+bytes[counter1+2]+bytes[counter1+1]
                    _68offset_to_dict_1 = hex(int(_68offset,16)+1)
                    _68offset_to_dict = hex(int(_68offset,16))
                    if _68offset_to_dict in ascii_dict:
                        after_instruction = _68offset
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; str: "+str(ascii_dict[_68offset_to_dict])
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; str: {bcolors.WARNING}"+str(ascii_dict[_68offset_to_dict])
                    elif _68offset_to_dict_1 in ascii_dict:
                        after_instruction = _68offset
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; str: "+str(ascii_dict[_68offset_to_dict_1])
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; str: {bcolors.WARNING}"+str(ascii_dict[_68offset_to_dict_1])
                    else:
                        after_instruction = _68offset
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(4)

                elif i == "04": # ADD al, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = " al, "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "08": # OR
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="00":
                        after_instruction = " byte [eax], al"
                    elif bytes[counter1+1]=="01":
                        after_instruction = " byte [ecx], al"
                    elif bytes[counter1+1]=="02":
                        after_instruction = " byte [edx], al"
                    elif bytes[counter1+1]=="03":
                        after_instruction = " byte [ebx], al"
                    elif bytes[counter1+1]=="06":
                        after_instruction = " byte [esi], al"
                    elif bytes[counter1+1]=="07":
                        after_instruction = " byte [edi], al"
                    elif bytes[counter1+1]=="08":
                        after_instruction = " byte [eax], cl"
                    elif bytes[counter1+1]=="09":
                        after_instruction = " byte [ecx], cl"
                    elif bytes[counter1+1]=="0A":
                        after_instruction = " byte [edx], cl"
                    elif bytes[counter1+1]=="0B":
                        after_instruction = " byte [ebx], cl"
                    elif bytes[counter1+1]=="0E":
                        after_instruction = " byte [esx], cl"
                    elif bytes[counter1+1]=="0F":
                        after_instruction = " byte [edi], cl"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "0A": # OR
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="36":
                        after_instruction = " dh, byte [esi]"
                    elif bytes[counter1+1]=="00":
                        after_instruction = " al, byte [eax]"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "0B": # OR
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="00":
                        after_instruction = " eax, dword [eax]"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "0C": # OR al, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = " al, "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "20": # AND
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="00":
                        after_instruction = " byte [eax], al"
                    elif bytes[counter1+1]=="01":
                        after_instruction = " byte [ecx], al"
                    elif bytes[counter1+1]=="02":
                        after_instruction = " byte [edx], al"
                    elif bytes[counter1+1]=="03":
                        after_instruction = " byte [ebx], al"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "24": # AND al, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = ", "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "29": # SUB
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="C6":
                        after_instruction = " esi, eax"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "2C": # SUB al, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = ", "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "30": # XOR
                    after_byte = " "+bytes[counter1+1]
                    XOR30var = 1
                    if bytes[counter1+1]=="00":
                        after_instruction = " byte [eax], al"
                    elif bytes[counter1+1]=="4D":
                        XOR30var2 = str(bytes[counter1+2])
                        if str(bytes[counter1+2][0])=="0":
                            XOR30var2 = str(bytes[counter1+2][1])
                        after_instruction = " byte [ebp + 0x"+XOR30var2+"], cl"
                        XOR30var = 2
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(XOR30var)

                elif i == "31": # XOR
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="ED":
                        after_instruction = " ebp, ebp"
                    elif bytes[counter1+1]=="FF":
                        after_instruction = " edi, edi"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "32": # XOR
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="00":
                        after_instruction = " al, byte [eax]"
                    elif bytes[counter1+1]=="2E":
                        after_instruction = " ch, byte [esi]"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "34": # XOR al, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = " al, "+"0x"+str(BAvar.lower())
                    lenWholeOpcode = len(instruction)+len(after_instruction)
                    if isClean:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(BAvar,16))
                    else:
                        after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(BAvar,16))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "85": # TEST
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="C0":
                        after_instruction = " eax, eax"
                    elif bytes[counter1+1]=="C1":
                        after_instruction = " ecx, eax"
                    elif bytes[counter1+1]=="C2":
                        after_instruction = " edx, eax"
                    elif bytes[counter1+1]=="C3":
                        after_instruction = " ebx, eax"
                    elif bytes[counter1+1]=="C4":
                        after_instruction = " esp, eax"
                    elif bytes[counter1+1]=="C5":
                        after_instruction = " ebp, eax"
                    elif bytes[counter1+1]=="C6":
                        after_instruction = " esi, eax"
                    elif bytes[counter1+1]=="C7":
                        after_instruction = " edi, eax"
                    elif bytes[counter1+1]=="C8":
                        after_instruction = " eax, ecx"
                    elif bytes[counter1+1]=="C9":
                        after_instruction = " ecx, ecx"
                    elif bytes[counter1+1]=="CA":
                        after_instruction = " edx, ecx"
                    elif bytes[counter1+1]=="CB":
                        after_instruction = " ebx, ecx"
                    elif bytes[counter1+1]=="CC":
                        after_instruction = " esp, ecx"
                    elif bytes[counter1+1]=="CD":
                        after_instruction = " ebp, ecx"
                    elif bytes[counter1+1]=="CE":
                        after_instruction = " esi, ecx"
                    elif bytes[counter1+1]=="CF":
                        after_instruction = " edi, ecx"
                    elif bytes[counter1+1]=="D0":
                        after_instruction = " eax, edx"
                    elif bytes[counter1+1]=="D1":
                        after_instruction = " ecx, edx"
                    elif bytes[counter1+1]=="D2":
                        after_instruction = " edx, edx"
                    elif bytes[counter1+1]=="D3":
                        after_instruction = " ebx, edx"
                    elif bytes[counter1+1]=="D4":
                        after_instruction = " esp, edx"
                    elif bytes[counter1+1]=="D5":
                        after_instruction = " ebp, edx"
                    elif bytes[counter1+1]=="D6":
                        after_instruction = " esi, edx"
                    elif bytes[counter1+1]=="D7":
                        after_instruction = " edi, edx"
                    elif bytes[counter1+1]=="D8":
                        after_instruction = " eax, ebx"
                    elif bytes[counter1+1]=="D9":
                        after_instruction = " ecx, ebx"
                    elif bytes[counter1+1]=="DA":
                        after_instruction = " edx, ebx"
                    elif bytes[counter1+1]=="DB":
                        after_instruction = " ebx, ebx"
                    elif bytes[counter1+1]=="DC":
                        after_instruction = " esp, ebx"
                    elif bytes[counter1+1]=="DD":
                        after_instruction = " ebp, ebx"
                    elif bytes[counter1+1]=="DE":
                        after_instruction = " esi, ebx"
                    elif bytes[counter1+1]=="DF":
                        after_instruction = " edi, ebx"
                    elif bytes[counter1+1]=="E0":
                        after_instruction = " eax, esp"
                    elif bytes[counter1+1]=="E1":
                        after_instruction = " ecx, esp"
                    elif bytes[counter1+1]=="E2":
                        after_instruction = " edx, esp"
                    elif bytes[counter1+1]=="E3":
                        after_instruction = " ebx, esp"
                    elif bytes[counter1+1]=="E4":
                        after_instruction = " esp, esp"
                    elif bytes[counter1+1]=="E5":
                        after_instruction = " ebp, esp"
                    elif bytes[counter1+1]=="E6":
                        after_instruction = " esi, esp"
                    elif bytes[counter1+1]=="E7":
                        after_instruction = " edi, esp"
                    elif bytes[counter1+1]=="E8":
                        after_instruction = " eax, ebp"
                    elif bytes[counter1+1]=="E9":
                        after_instruction = " ecx, ebp"
                    elif bytes[counter1+1]=="EA":
                        after_instruction = " edx, ebp"
                    elif bytes[counter1+1]=="EB":
                        after_instruction = " ebx, ebp"
                    elif bytes[counter1+1]=="EC":
                        after_instruction = " esp, ebp"
                    elif bytes[counter1+1]=="ED":
                        after_instruction = " ebp, ebp"
                    elif bytes[counter1+1]=="EE":
                        after_instruction = " esi, ebp"
                    elif bytes[counter1+1]=="EF":
                        after_instruction = " edi, ebp"
                    elif bytes[counter1+1]=="F0":
                        after_instruction = " eax, esi"
                    elif bytes[counter1+1]=="F1":
                        after_instruction = " ecx, esi"
                    elif bytes[counter1+1]=="F2":
                        after_instruction = " edx, esi"
                    elif bytes[counter1+1]=="F3":
                        after_instruction = " ebx, esi"
                    elif bytes[counter1+1]=="F4":
                        after_instruction = " esp, esi"
                    elif bytes[counter1+1]=="F5":
                        after_instruction = " ebp, esi"
                    elif bytes[counter1+1]=="F6":
                        after_instruction = " esi, esi"
                    elif bytes[counter1+1]=="F7":
                        after_instruction = " edi, esi"
                    elif bytes[counter1+1]=="F8":
                        after_instruction = " eax, edi"
                    elif bytes[counter1+1]=="F9":
                        after_instruction = " ecx, edi"
                    elif bytes[counter1+1]=="FA":
                        after_instruction = " edx, edi"
                    elif bytes[counter1+1]=="FB":
                        after_instruction = " ebx, edi"
                    elif bytes[counter1+1]=="FC":
                        after_instruction = " esp, edi"
                    elif bytes[counter1+1]=="FD":
                        after_instruction = " ebp, edi"
                    elif bytes[counter1+1]=="FE":
                        after_instruction = " esi, edi"
                    elif bytes[counter1+1]=="FF":
                        after_instruction = " edi, edi"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "84": # TEST
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="C0":
                        after_instruction = " al, al"
                    elif bytes[counter1+1]=="C1":
                        after_instruction = " cl, al"
                    elif bytes[counter1+1]=="C2":
                        after_instruction = " dl, al"
                    elif bytes[counter1+1]=="C3":
                        after_instruction = " bl, al"
                    elif bytes[counter1+1]=="C4":
                        after_instruction = " ah, al"
                    elif bytes[counter1+1]=="C5":
                        after_instruction = " ch, al"
                    elif bytes[counter1+1]=="C6":
                        after_instruction = " dh, al"
                    elif bytes[counter1+1]=="C7":
                        after_instruction = " bh, al"
                    elif bytes[counter1+1]=="C8":
                        after_instruction = " al, cl"
                    elif bytes[counter1+1]=="C9":
                        after_instruction = " cl, cl"
                    elif bytes[counter1+1]=="CA":
                        after_instruction = " dl, cl"
                    elif bytes[counter1+1]=="CB":
                        after_instruction = " bl, cl"
                    elif bytes[counter1+1]=="CC":
                        after_instruction = " ah, cl"
                    elif bytes[counter1+1]=="CD":
                        after_instruction = " ch, cl"
                    elif bytes[counter1+1]=="CE":
                        after_instruction = " dh, cl"
                    elif bytes[counter1+1]=="CF":
                        after_instruction = " bh, cl"
                    elif bytes[counter1+1]=="D0":
                        after_instruction = " al, dl"
                    elif bytes[counter1+1]=="D1":
                        after_instruction = " cl, dl"
                    elif bytes[counter1+1]=="D2":
                        after_instruction = " dl, dl"
                    elif bytes[counter1+1]=="D3":
                        after_instruction = " bl, dl"
                    elif bytes[counter1+1]=="D4":
                        after_instruction = " ah, dl"
                    elif bytes[counter1+1]=="D5":
                        after_instruction = " ch, dl"
                    elif bytes[counter1+1]=="D6":
                        after_instruction = " dh, dl"
                    elif bytes[counter1+1]=="D7":
                        after_instruction = " bh, dl"
                    elif bytes[counter1+1]=="D8":
                        after_instruction = " al, bl"
                    elif bytes[counter1+1]=="D9":
                        after_instruction = " cl, bl"
                    elif bytes[counter1+1]=="DA":
                        after_instruction = " dl, bl"
                    elif bytes[counter1+1]=="DB":
                        after_instruction = " bl, bl"
                    elif bytes[counter1+1]=="DC":
                        after_instruction = " ah, bl"
                    elif bytes[counter1+1]=="DD":
                        after_instruction = " ch, bl"
                    elif bytes[counter1+1]=="DE":
                        after_instruction = " dh, bl"
                    elif bytes[counter1+1]=="DF":
                        after_instruction = " bh, bl"
                    elif bytes[counter1+1]=="E0":
                        after_instruction = " al, ah"
                    elif bytes[counter1+1]=="E1":
                        after_instruction = " cl, ah"
                    elif bytes[counter1+1]=="E2":
                        after_instruction = " dl, ah"
                    elif bytes[counter1+1]=="E3":
                        after_instruction = " bl, ah"
                    elif bytes[counter1+1]=="E4":
                        after_instruction = " ah, ah"
                    elif bytes[counter1+1]=="E5":
                        after_instruction = " ch, ah"
                    elif bytes[counter1+1]=="E6":
                        after_instruction = " dh, ah"
                    elif bytes[counter1+1]=="E7":
                        after_instruction = " bh, ah"
                    elif bytes[counter1+1]=="E8":
                        after_instruction = " al, ch"
                    elif bytes[counter1+1]=="E9":
                        after_instruction = " cl, ch"
                    elif bytes[counter1+1]=="EA":
                        after_instruction = " dl, ch"
                    elif bytes[counter1+1]=="EB":
                        after_instruction = " bl, ch"
                    elif bytes[counter1+1]=="EC":
                        after_instruction = " ah, ch"
                    elif bytes[counter1+1]=="ED":
                        after_instruction = " ch, ch"
                    elif bytes[counter1+1]=="EE":
                        after_instruction = " dh, ch"
                    elif bytes[counter1+1]=="EF":
                        after_instruction = " bh, ch"
                    elif bytes[counter1+1]=="F0":
                        after_instruction = " al, dh"
                    elif bytes[counter1+1]=="F1":
                        after_instruction = " cl, dh"
                    elif bytes[counter1+1]=="F2":
                        after_instruction = " dl, dh"
                    elif bytes[counter1+1]=="F3":
                        after_instruction = " bl, dh"
                    elif bytes[counter1+1]=="F4":
                        after_instruction = " ah, dh"
                    elif bytes[counter1+1]=="F5":
                        after_instruction = " ch, dh"
                    elif bytes[counter1+1]=="F6":
                        after_instruction = " dh, dh"
                    elif bytes[counter1+1]=="F7":
                        after_instruction = " bh, dh"
                    elif bytes[counter1+1]=="F8":
                        after_instruction = " al, bh"
                    elif bytes[counter1+1]=="F9":
                        after_instruction = " cl, bh"
                    elif bytes[counter1+1]=="FA":
                        after_instruction = " dl, bh"
                    elif bytes[counter1+1]=="FB":
                        after_instruction = " bl, bh"
                    elif bytes[counter1+1]=="FC":
                        after_instruction = " ah, bh"
                    elif bytes[counter1+1]=="FD":
                        after_instruction = " ch, bh"
                    elif bytes[counter1+1]=="FE":
                        after_instruction = " dh, bh"
                    elif bytes[counter1+1]=="FF":
                        after_instruction = " bh, bh"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "81": # ADD, ...
                    after_byte = " "+bytes[counter1+1]+" "+bytes[counter1+2]+" "+bytes[counter1+3]+" "+bytes[counter1+4]+" "+bytes[counter1+5]
                    _81var = ""
                    if bytes[counter1+1]=="C3":
                        if bytes[counter1+5]!="00":
                            _81var += str(bytes[counter1+5])
                        if bytes[counter1+4]!="00":
                            _81var += str(bytes[counter1+4])
                        if bytes[counter1+3]!="00":
                            _81var += str(bytes[counter1+3])
                        if bytes[counter1+2]!="00":
                            _81var += str(bytes[counter1+2])
                        after_instruction = " ebx, 0x"+_81var
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(_81var,16))
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(_81var,16))
                    elif bytes[counter1+1]=="EC":
                        instruction = "SUB"
                        if bytes[counter1+5]!="00":
                            _81var += str(bytes[counter1+5])
                        if bytes[counter1+4]!="00":
                            _81var += str(bytes[counter1+4])
                        if bytes[counter1+3]!="00":
                            _81var += str(bytes[counter1+3])
                        if bytes[counter1+2]!="00":
                            _81var += str(bytes[counter1+2])
                        after_instruction = " esp, 0x"+_81var
                        lenWholeOpcode = len(instruction)+len(after_instruction)
                        if isClean:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+"; "+str(int(_81var,16))
                        else:
                            after_instruction = after_instruction+" "*(32-lenWholeOpcode)+f"{bcolors.OKGREEN}; "+str(int(_81var,16))
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(5)

                elif i == "F3": # RET
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="C3":
                        pass
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "F6": # NOT, NEG, IDIV, DIV, IMUL, MUL
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="FF":
                        instruction = "IDIV"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="FE":
                        instruction = "IDIV"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="FD":
                        instruction = "IDIV"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="FC":
                        instruction = "IDIV"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="FB":
                        instruction = "IDIV"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="FA":
                        instruction = "IDIV"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="F9":
                        instruction = "IDIV"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="F8":
                        instruction = "IDIV"
                        after_instruction = " al"
                    elif bytes[counter1+1]=="F7":
                        instruction = "DIV"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="F6":
                        instruction = "DIV"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="F5":
                        instruction = "DIV"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="F4":
                        instruction = "DIV"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="F3":
                        instruction = "DIV"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="F2":
                        instruction = "DIV"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="F1":
                        instruction = "DIV"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="F0":
                        instruction = "DIV"
                        after_instruction = " al"
                    elif bytes[counter1+1]=="EF":
                        instruction = "IMUL"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="EE":
                        instruction = "IMUL"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="ED":
                        instruction = "IMUL"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="EC":
                        instruction = "IMUL"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="EB":
                        instruction = "IMUL"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="EA":
                        instruction = "IMUL"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="E9":
                        instruction = "IMUL"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="E8":
                        instruction = "IMUL"
                        after_instruction = " al"
                    elif bytes[counter1+1]=="E7":
                        instruction = "MUL"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="E6":
                        instruction = "MUL"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="E5":
                        instruction = "MUL"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="E4":
                        instruction = "MUL"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="E3":
                        instruction = "MUL"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="E2":
                        instruction = "MUL"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="E1":
                        instruction = "MUL"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="E0":
                        instruction = "MUL"
                        after_instruction = " al"
                    elif bytes[counter1+1]=="DF":
                        instruction = "NEG"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="DE":
                        instruction = "NEG"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="DD":
                        instruction = "NEG"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="DC":
                        instruction = "NEG"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="DB":
                        instruction = "NEG"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="DA":
                        instruction = "NEG"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="D9":
                        instruction = "NEG"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="D8":
                        instruction = "NEG"
                        after_instruction = " al"
                    elif bytes[counter1+1]=="D7":
                        instruction = "NOT"
                        after_instruction = " bh"
                    elif bytes[counter1+1]=="D6":
                        instruction = "NOT"
                        after_instruction = " dh"
                    elif bytes[counter1+1]=="D5":
                        instruction = "NOT"
                        after_instruction = " ch"
                    elif bytes[counter1+1]=="D4":
                        instruction = "NOT"
                        after_instruction = " ah"
                    elif bytes[counter1+1]=="D3":
                        instruction = "NOT"
                        after_instruction = " bl"
                    elif bytes[counter1+1]=="D2":
                        instruction = "NOT"
                        after_instruction = " dl"
                    elif bytes[counter1+1]=="D1":
                        instruction = "NOT"
                        after_instruction = " cl"
                    elif bytes[counter1+1]=="D0":
                        instruction = "NOT"
                        after_instruction = " al"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "F7": # NOT, NEG, IDIV, DIV, IMUL, MUL
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="FF":
                        instruction = "IDIV"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="FE":
                        instruction = "IDIV"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="FD":
                        instruction = "IDIV"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="FC":
                        instruction = "IDIV"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="FB":
                        instruction = "IDIV"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="FA":
                        instruction = "IDIV"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="F9":
                        instruction = "IDIV"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="F8":
                        instruction = "IDIV"
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="F7":
                        instruction = "DIV"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="F6":
                        instruction = "DIV"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="F5":
                        instruction = "DIV"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="F4":
                        instruction = "DIV"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="F3":
                        instruction = "DIV"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="F2":
                        instruction = "DIV"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="F1":
                        instruction = "DIV"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="F0":
                        instruction = "DIV"
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="EF":
                        instruction = "IMUL"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="EE":
                        instruction = "IMUL"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="ED":
                        instruction = "IMUL"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="EC":
                        instruction = "IMUL"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="EB":
                        instruction = "IMUL"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="EA":
                        instruction = "IMUL"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="E9":
                        instruction = "IMUL"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="E8":
                        instruction = "IMUL"
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="E7":
                        instruction = "MUL"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="E6":
                        instruction = "MUL"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="E5":
                        instruction = "MUL"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="E4":
                        instruction = "MUL"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="E3":
                        instruction = "MUL"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="E2":
                        instruction = "MUL"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="E1":
                        instruction = "MUL"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="E0":
                        instruction = "MUL"
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="DF":
                        instruction = "NEG"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="DE":
                        instruction = "NEG"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="DD":
                        instruction = "NEG"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="DC":
                        instruction = "NEG"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="DB":
                        instruction = "NEG"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="DA":
                        instruction = "NEG"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="D9":
                        instruction = "NEG"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="D8":
                        instruction = "NEG"
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="D7":
                        instruction = "NOT"
                        after_instruction = " edi"
                    elif bytes[counter1+1]=="D6":
                        instruction = "NOT"
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="D5":
                        instruction = "NOT"
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="D4":
                        instruction = "NOT"
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="D3":
                        instruction = "NOT"
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="D2":
                        instruction = "NOT"
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="D1":
                        instruction = "NOT"
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="D0":
                        instruction = "NOT"
                        after_instruction = " eax"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "FF": # CALL
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="D0":
                        after_instruction = " eax"
                    elif bytes[counter1+1]=="D1":
                        after_instruction = " ecx"
                    elif bytes[counter1+1]=="D2":
                        after_instruction = " edx"
                    elif bytes[counter1+1]=="D3":
                        after_instruction = " ebx"
                    elif bytes[counter1+1]=="D4":
                        after_instruction = " esp"
                    elif bytes[counter1+1]=="D5":
                        after_instruction = " ebp"
                    elif bytes[counter1+1]=="D6":
                        after_instruction = " esi"
                    elif bytes[counter1+1]=="D7":
                        after_instruction = " edi"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(1)

                elif i == "0F": # PUSH fs, PUSH gs, POP fs, POP gs, ...
                    ofvar1 = 1
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="A0":
                        instruction = "PUSH"
                        after_instruction = " fs"
                    elif bytes[counter1+1]=="A8":
                        instruction = "PUSH"
                        after_instruction = " gs"
                    elif bytes[counter1+1]=="A1":
                        instruction = "POP"
                        after_instruction = " fs"
                    elif bytes[counter1+1]=="A9":
                        instruction = "POP"
                        after_instruction = " gs"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    intruction_len_for_check = 51+len(instruction)+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    if isClean:
                        bcolors = colors
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+instruction+after_instruction+f"{bcolors.RESET}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    if should_print:
                        cancle_function_iteration(ofvar1)
                    
            else:
                pass
                #bcolors = colors
                #print(f"{bcolors.OKBLUE}"+str(hex(offset1))+"  "+f"{bcolors.FAIL}"+to_display+"                 "+f"{bcolors.WARNING}"+"???"+f"{bcolors.RESET}")

        else:
            times -= 1
        
        offset1 += 1
        counter1 += 1

    return True
