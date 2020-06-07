# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",            # DONE?    # next byte represents how much instructions to jump (+2). Example: 74 05 -> JE <ADDRESS OF THIS INSTRUCTION>+7 (05+2=7)
    "75" : "JNE",           # DONE?    # next byte represents how much instructions to jump (+2). Example: 75 05 -> JNE <ADDRESS OF THIS INSTRUCTION>+7 (05+2=7)
    "7E" : "JLE",           # PENDING   need to add more info
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
    "41" : "INC ecx",       # PENDING
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
    "B8" : "MOV eax",       # PENDING  # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xGHEFCDAB
    "BA" : "MOV edx",       # DONE?    # next byte represents MOV value
    "8B" : "MOV",           # DONE?    # if next byte is equal to 1C then: MOV ebx, dword [esp]
                                       #             -||-      to 10 then: MOV edx, dword [eax]
                                       #             -||-      to 55 then: MOV edx, dword [var_4h]
                                       #             -||-      to 45 then: MOV eax, dword [arg_8h]
                                       #             -||-      to 4D then: MOV ecx, dword [var_4h]
                                       #             -||-      to 00 then: MOV eax, dword [eax]
                                       #             -||-      to 6C then: MOV ebp, dword [arg_4h]
                                       #             -||-      to 43 then: MOV eax, dword [ebx + <VALUE>] where <VALUE> is equal to byte after 43
    "89" : "MOV ebp",       # DONE?    # if byte is equal to 89 then check if next byte is equal to E5 / if the next byte is equal to E5 then "MOV ebp, esp"
    "01" : "ADD",           # DONE?    # if next byte is equal to CA then: ADD EDX, ECX
                                       #             -||-      to D0 then: ADD EAX, EDX
    "83" : "ADD",           # DONE?    # if nexy byte is equal to C2 then: ADD EDX, <value>  where VALUE is equal to byte after C2
                            # DONE?    #             -||-      to C7 then: ADD EDI, <VALUE>             -||-
                            # DONE?    #             -||-      to C4 then: ADD ESP, <VALUE>             -||-
                            # DONE?    #             -||-      to C0 then: ADD EAX, <VALUE>             -||-
                            # PENDING  #             -||-      to E4 then: AND ESP, <VALUE>             -||-                        need to add more info
                            # DONE?    #             -||-      to F8 then: CMP EAX, <VALUE>             -||-
                            # DONE?    #             -||-      to 3B then: CMP DWORD [EBX], <VALUE>     -||-
                            # PENDING  #             -||-      to 7D 08 then: CMP DWORD [ARG_8H], <VALUE>     -||-                  need to add more info
                            # DONE?    #             -||-      to EC then: SUB ESP, <VALUE>             -||-
                            # DONE?    #             -||-      to EA then: SUB EDX, <VALUE>             -||-
                            # DONE?    #             -||-      to 08 then: OR DWORD [EAX], <VALUE>      -||-                        need to add more info
                            # DONE?    # if next 2 bytes: 45 FC <value> then: ADD DWORD [var_4h], <value>
                            # PENDING  # if next 2 bytes: 7D 08 <value> then: CMP DWORD [arg_8h], <value>
    "90" : "NOP",           # DONE
    "81" : "ADD",           # PENDING  # if next                       need to add more info

    "0F" : "INSTRUCTION",   # PENDING
}

x860Fopcodes = {

    "84" : "JE",            # PENDING                                  need to add more info
    "A0" : "PUSH fs",       # PENDING
    "A8" : "PUSH gs",       # PENDING
    "A1" : "POP fs",        # PENDING
    "A9" : "POP gs",        # PENDING
}
