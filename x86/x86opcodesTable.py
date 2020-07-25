# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 74 05 -> JE <ADDRESS OF THIS INSTRUCTION>+7 (int('05',16)+2=7)    # + logic behind reverse jumps: if 2nd byte>128
    "75" : "JNE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 75 05 -> JNE <ADDRESS OF THIS INSTRUCTION>+7 (int('05',16)+2=7)   # + logic behind reverse jumps: if 2nd byte>128
    "7E" : "JLE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 7E 2C -> JLE <ADDRESS OF THIS INSTRUCTION>+46 (int('2C',16)+2=46) # + logic behind reverse jumps: if 2nd byte>128
    "7F" : "JG",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 7F 1D -> JG <ADDRESS OF THIS INSTRUCTION>+31 (int('1D',16)+2=31) # + logic behind reverse jumps: if 2nd byte>128
    "70" : "JO",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 70 0E -> JO <ADDRESS OF THIS INSTRUCTION>+16 (int('0E',16)+2=16) # + logic behind reverse jumps: if 2nd byte>128
    "71" : "JNO",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JNO <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "72" : "JB",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JB <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "73" : "JAE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JAE <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "31" : "XOR",           # DONE?    # if next byte is equal to ED then: XOR ebp, ebp
                            # DONE?    #           -||-        to FF then: XOR edi, edi
    "0C" : "OR",            # DONE?    # next byte represents or value: OR al, <VALUE>
    "4C" : "DEC esp",       # DONE
    "49" : "DEC ecx",       # DONE
    "4E" : "DEC esi",       # DONE
    "4F" : "DEC edi",       # DONE
    "48" : "DEC eax",       # DONE
    "46" : "INC esi",       # DONE
    "44" : "INC esp",       # DONE
    "47" : "INC edi",       # DONE
    "42" : "INC edx",       # DONE
    "43" : "INC ebx",       # DONE
    "40" : "INC eax",       # DONE
    "41" : "INC ecx",       # DONE
    "50" : "PUSH eax",      # DONE
    "51" : "PUSH ecx",      # DONE
    "52" : "PUSH edx",      # DONE
    "53" : "PUSH ebx",      # DONE
    "54" : "PUSH esp",      # DONE
    "55" : "PUSH ebp",      # DONE
    "56" : "PUSH esi",      # DONE
    "57" : "PUSH edi",      # DONE
    "0E" : "PUSH cs",       # DONE
    "16" : "PUSH ss",       # DONE
    "1E" : "PUSH ds",       # DONE
    "06" : "PUSH es",       # DONE
    "68" : "PUSH",          # DONE?    # next 4 bytes represents *string* address, in format: AB CD EF GH -> GH EF CD AB
    "1F" : "POP ds",        # DONE
    "07" : "POP es",        # DONE
    "17" : "POP ss",        # DONE
    "58" : "POP eax",       # DONE
    "59" : "POP ecx",       # DONE
    "5A" : "POP edx",       # DONE
    "5B" : "POP ebx",       # DONE
    "5C" : "POP esp",       # DONE
    "5D" : "POP ebp",       # DONE
    "5E" : "POP esi",       # DONE
    "5F" : "POP edi",       # DONE
    "61" : "POPAL",         # DONE     
    "C9" : "LEAVE",         # DONE
    "C3" : "RET",           # DONE
    "F3" : "RET",           # DONE?    # if next byte is equal to C3 then: RET
    "00" : "ADD",           # PENDING  # if next byte is equal to 00 then: ADD byte [eax], al       # this instruction will be added at the end 
    "B8" : "MOV eax",       # PENDING  # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xGHEFCDAB
    "BA" : "MOV edx",       # DONE?    # next byte represents MOV value
    "8B" : "MOV",           # DONE?    # if next byte is equal to 1C then: MOV ebx, dword [esp]
                            # DONE?    #             -||-      to 10 then: MOV edx, dword [eax]
                            # DONE?    #             -||-      to 55 then: MOV edx, dword [var_4h]
                            # DONE?    #             -||-      to 45 then: MOV eax, dword [arg_8h]
                            # DONE?    #             -||-      to 4D then: MOV ecx, dword [var_4h]
                            # DONE?    #             -||-      to 00 then: MOV eax, dword [eax]
                            # DONE?    #             -||-      to 6C then: MOV ebp, dword [arg_4h]
                            # DONE?    #             -||-      to 43 then: MOV eax, dword [ebx + <VALUE>] where <VALUE> is equal to byte after 43
    "89" : "MOV",           # DONE?    # if next byte is equal to E5 then: MOV ebp, esp
                            # DONE?    #             -||-      to CB then: MOV ebx, ecx
    "01" : "ADD",           # DONE?    # if next byte is equal to CA then: ADD EDX, ECX
                            # DONE?    #             -||-      to D0 then: ADD EAX, EDX
                            # DONE?    #             -||-      to 01 then: ADD dword [ecx], eax
                            # DONE?    #             -||-      to 00 then: ADD dword [eax], eax
    "83" : "ADD",           # DONE?    # if nexy byte is equal to C2 then: ADD EDX, <value>  where VALUE is equal to byte after C2
                            # DONE?    #             -||-      to C7 then: ADD EDI, <VALUE>             -||-
                            # DONE?    #             -||-      to C4 then: ADD ESP, <VALUE>             -||-
                            # DONE?    #             -||-      to C0 then: ADD EAX, <VALUE>             -||-
                            # DONE?    #             -||-      to E4 then: AND ESP, <VALUE>             -||-
                            # DONE?    #             -||-      to F8 then: CMP EAX, <VALUE>             -||-
                            # DONE?    #             -||-      to 3B then: CMP DWORD [EBX], <VALUE>     -||-
                            # DONE?    #             -||-      to EC then: SUB ESP, <VALUE>             -||-
                            # DONE?    #             -||-      to EA then: SUB EDX, <VALUE>             -||-
                            # DONE?    #             -||-      to 08 then: OR DWORD [EAX], <VALUE>      -||-
                            # DONE?    # if next 2 bytes: 45 FC <value> then: ADD DWORD [var_4h], <value>
                            # DONE?    # if next 2 bytes: 7D 08 <value> then: CMP DWORD [arg_8h], <value>
    "90" : "NOP",           # DONE
    "81" : "ADD",           # PENDING  # if next byte is equal to C3 then: ADD ebx, <value> where VALUE is (hexadecimal, and) equal to next for bytes in this format: GH EF CD AB
                            # PENDING  #             -||-      to EC then: SUB esp, <value>                                  -||-
    "04" : "ADD",           # DONE?    # next byte represents add value: ADD al, <VALUE>
    "FF" : "CALL",          # DONE?    # if next byte is equal to d0 then: CALL eax    # FF is also associated with JMP, INC, need to add more info
                            # DONE?    #             -||-      to d1 then: CALL ecx
                            # DONE?    #             -||-      to d2 then: CALL edx
                            # DONE?    #             -||-      to d3 then: CALL ebx
                            # DONE?    #             -||-      to d4 then: CALL esp
                            # DONE?    #             -||-      to d5 then: CALL ebp
                            # DONE?    #             -||-      to d6 then: CALL esi
                            # DONE?    #             -||-      to d7 then: CALL edi
    "E8" : "CALL",          # PENDING  # need to add more info
    "0F" : "INSTRUCTION",   # PENDING
}

x860Fopcodes = {

    "84" : "JE",            # PENDING  # need to add more info
    "A0" : "PUSH fs",       # DONE?
    "A8" : "PUSH gs",       # DONE?
    "A1" : "POP fs",        # DONE?
    "A9" : "POP gs",        # DONE?
}
