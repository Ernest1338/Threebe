# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {

    "74" : "JE",
    "55" : "PUSH ebp",
    "B8" : "MOV eax", # next bite represents MOV value / if 4 next bites are not instructions, then those bites represent an adress in format: B8 AB CD EF GH > MOV eax, 0xHGFCDAB
    "89" : "MOV ebp" # if bite is equal to 89 then check if next bite is equal to E5 / if the next bite is equal to E5 then "MOV ebp, esp"
}
