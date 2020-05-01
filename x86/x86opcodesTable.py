# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",         # DONE?
    "75" : "JNE",        # PENDING
    "50" : "PUSH eax",   # DONE
    "51" : "PUSH ecx",   # DONE
    "52" : "PUSH edx",   # DONE
    "53" : "PUSH ebx",   # DONE
    "54" : "PUSH esp",   # DONE
    "55" : "PUSH ebp",   # DONE
    "56" : "PUSH esi",   # DONE
    "57" : "PUSH edi",   # DONE
    "0E" : "PUSH cs",    # DONE
    "16" : "PUSH ss",    # DONE
    "1E" : "PUSH ds",    # DONE
    "06" : "PUSH es",    # DONE
    "B8" : "MOV eax",    # PENDING  # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xHGFCDAB
    "89" : "MOV ebp",    # PENDING  # if byte is equal to 89 then check if next byte is equal to E5 / if the next byte is equal to E5 then "MOV ebp, esp"
    "01" : "ADD",        # DONE?    # if next byte is equal to CA then: ADD EDX, ECX
                                    #             -||-      to D0 then: ADD EAX, EDX
    "83" : "ADD",        # PENDING  # if nexy byte is equal to C2 then: ADD EDX, <value>  where VALUE is equal to byte after C2
                                    #             -||-      to C4 then: ADD ESP, <VALUE>             -||-
                                    #             -||-      to C7 then: ADD EDI, <VALUE>             -||-
                                    # if next 2 bytes: 45 FC <value> then: ADD DWORD [var_4h], <value>
    "90" : "NOP",        # DONE
    "81" : "ADD",        # PENDING  # if next

    "0F" : "INSTRUCTION",# PENDING
}

x860Fopcodes = {

    "84" : "JE",         # PENDING
    "A0" : "PUSH fs",    # PENDING
    "A8" : "PUSH gs",    # PENDING
}
