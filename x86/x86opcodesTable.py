# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",
    "75" : "JNE",
    "55" : "PUSH ebp",
    "B8" : "MOV eax", # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xHGFCDAB
    "89" : "MOV ebp", # if byte is equal to 89 then check if next byte is equal to E5 / if the next byte is equal to E5 then "MOV ebp, esp"
    "0F" : "INSTRUCTION",
}

x860Fopcodes = {

    "84" : "JE",

}
