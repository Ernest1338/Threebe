import x86.x86opcodesTable as x86opT
from hexdump.hexdump import bcolors

times = 0

def cancle_function_iteration(howmany):
    global times
    times += int(howmany)

def disassemble(bytes):
    global times
    offset1 = 2152202240
    counter1 = 0
    for i in bytes:
        if times == 0:
            to_display = i
            after_instruction = ""
            after_byte = ""
            if i in x86opT.x86opcodes:
                if i == "74": # JE
                    after_byte = " "+bytes[counter1+1]
                    after_instruction = " "+hex(offset1+(int(bytes[counter1+1],16)+2))
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    if len(check1) < 63:
                        for _ in range(63-len(check1)):
                            after_byte += " "
                    check1 = f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+after_byte+f"{bcolors.WARNING}"+x86opT.x86opcodes[i]+after_instruction+f"{bcolors.ENDC}"
                    print(check1)
                    after_byte = ""
                    after_instruction = ""
                    cancle_function_iteration(1)
            else:
                #pass
                print(f"{bcolors.OKBLUE}"+str(hex(offset1))+"   "+f"{bcolors.FAIL}"+to_display+"                "+f"{bcolors.WARNING}"+"???"+f"{bcolors.ENDC}")
        else:
            times -= 1
        offset1 += 16
        counter1 += 1
    # print(x86opT.x86opcodes["55"])
    return True
