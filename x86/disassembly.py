import x86.x86opcodesTable as x86opT
from hexdump.hexdump import bcolors

times = 0

def cancle_function_iteration(howmany):
    global times
    times += int(howmany)

def disassemble(bytes):
    global times
    offset1 = 134512640
    counter1 = 0

    for i in bytes:

        if times == 0:
            to_display = i
            after_instruction = ""
            after_byte = ""

            if i in x86opT.x86opcodes:
                intruction_len_for_check = 50+len(x86opT.x86opcodes[i]) # need to add to this after_instruction every time this variable (after_instruction) is usesd inside an if
                should_print = True

                if i == "74": # JE
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
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif (i == "90" or i == "55" or i == "50" or i == "56" or i == "57" or i == "51" or i == "53" or i == "52" or i == "54" or i == "0E" or i == "16" or i == "1E" or i == "06"
                or i == "1F" or i == "07" or i == "17" or i == "58" or i == "59" or i == "5A" or i == "5B" or i == "5C" or i == "5D" or i == "5E" or i == "5F" or i == "61"): # NOP, PUSH (1 byte), POP
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""

                elif i == "01": # ADD
                    after_byte = " "+bytes[counter1+1]
                    if bytes[counter1+1]=="CA":
                        after_instruction = " edx, ecx"
                    elif bytes[counter1+1]=="D0":
                        after_instruction = " eax, edx"
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "BA": # MOV edx, <value>
                    after_byte = " "+bytes[counter1+1]
                    BAvar = bytes[counter1+1]
                    if bytes[counter1+1][0]=="0":
                        BAvar = bytes[counter1+1][1]
                    after_instruction = ", "+"0x"+str(BAvar)
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "89": # MOV ebp, esp
                    after_byte = " "+bytes[counter1+1]
                    _89var = bytes[counter1+1]
                    if _89var=="E5":
                        after_instruction = ", esp"
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)

                elif i == "8B": # MOV
                    after_byte = " "+bytes[counter1+1]
                    _8Bvar = 1
                    if bytes[counter1+1]=="1C":
                        after_instruction = " ebx, dword [esp]"
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
                        after_instruction = " eax, dword [ebx + "+str(bytes[counter1+2])+"]"
                        _8Bvar = 2
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(_8Bvar)

                elif i == "83": # ADD
                    after_byte = " "+bytes[counter1+1]+" "+bytes[counter1+2]
                    ADD83var = bytes[counter1+2]
                    if bytes[counter1+2][0]=="0":
                        ADD83var = bytes[counter1+2][1]
                    if bytes[counter1+1]=="C2":
                        after_instruction = " edx, "+"0x"+str(ADD83var.lower())
                    elif bytes[counter1+1]=="C4":
                        after_instruction = " esp, "+"0x"+str(ADD83var.lower())
                    elif bytes[counter1+1]=="C7":
                        after_instruction = " edi, "+"0x"+str(ADD83var.lower())
                    else:
                        should_print = False
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    if should_print:
                        print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(2)

                elif i == "75": # JNE
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
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    intruction_len_for_check = 50+len(x86opT.x86opcodes[i])+len(after_instruction)
                    if len(check1) < intruction_len_for_check:
                        for _ in range(intruction_len_for_check-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)
                    
            else:
                pass
                #print(f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+"                "+f"{bcolors.WARNING}"+"???"+f"{bcolors.ENDC}")

        else:
            times -= 1
        offset1 += 1
        counter1 += 1

    # print(x86opT.x86opcodes["55"])
    return True
