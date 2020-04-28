# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",
    "75" : "JNE",
    "55" : "PUSH ebp",
    "B8" : "MOV eax", # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xHGFCDAB
    "89" : "MOV ebp", # if byte is equal to 89 then check if next byte is equal to E5 / if the next byte is equal to E5 then "MOV ebp, esp"
    "01" : "ADD",   # if next byte is equal to CA then: ADD EDX, ECX
                    #             -||-      to D0 then: ADD EAX, EDX
    "83" : "ADD",   # next byte: if C2 then: ADD EDX, <value>   third byte: hex value to add
                    # if next 2 bytes: 45 FC <value> then: ADD DWORD [var_4h], <value>
    "90" : "NOP",

    "0F" : "INSTRUCTION",
}

x860Fopcodes = {

    "84" : "JE",

}
