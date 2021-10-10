# This file contain python dictionary of opcodes for x86 architecture

x86opcodes = {
    "00" : "ADD",           # PENDING  # if next byte is equal to 00 then: ADD byte [eax], al       # this instruction will be added at the end 
                            # PENDING  #             -||-      to F8 then: ADD al, bh
    "01" : "ADD",           # DONE?    # if next byte is equal to CA then: ADD edx, ecx
                            # DONE?    #             -||-      to D0 then: ADD eax, edx
                            # DONE?    #             -||-      to 01 then: ADD dword [ecx], eax
                            # DONE?    #             -||-      to 00 then: ADD dword [eax], eax
    "04" : "ADD",           # DONE?    # next byte represents add value: ADD al, <VALUE>
    "06" : "PUSH es",       # DONE
    "07" : "POP es",        # DONE
    "08" : "OR",            # DONE?    # if next byte is equal to 00 then: OR byte [eax], al
                            # DONE?    #           -||-        to 01 then: OR byte [ecx], al
                            # DONE?    #           -||-        to 02 then: OR byte [edx], al
                            # DONE?    #           -||-        to 03 then: OR byte [ebx], al
                            # DONE?    #           -||-        to 06 then: OR byte [esi], al
                            # DONE?    #           -||-        to 07 then: OR byte [edi], al
                            # DONE?    #           -||-        to 08 then: OR byte [eax], cl
                            # DONE?    #           -||-        to 09 then: OR byte [ecx], cl
                            # DONE?    #           -||-        to 0A then: OR byte [edx], cl
                            # DONE?    #           -||-        to 0B then: OR byte [ebx], cl
                            # DONE?    #           -||-        to 0E then: OR byte [esx], cl
                            # DONE?    #           -||-        to 0F then: OR byte [edi], cl
    "0A" : "OR",            # DONE?    # if next byte is equal to 36 then: OR dh, byte [esi]
                            # DONE?    #           -||-        to 00 then: OR al, byte [eax]
    "0B" : "OR",            # DONE?    # if next byte is equal to 00 then: OR eax, dword [eax]
    "0C" : "OR",            # DONE?    # next byte represents OR value: OR al, <VALUE>
    "0E" : "PUSH cs",       # DONE
    "0F" : "INSTRUCTION",   # WIP
    "16" : "PUSH ss",       # DONE
    "17" : "POP ss",        # DONE
    "1E" : "PUSH ds",       # DONE
    "1F" : "POP ds",        # DONE
    "20" : "AND",           # DONE?    # if next byte is equal to 00 then: AND byte [eax], al
                            # DONE?    #           -||-        to 01 then: AND byte [ecx], al
                            # DONE?    #           -||-        to 02 then: AND byte [edx], al
                            # DONE?    #           -||-        to 03 then: AND byte [ebx], al
    "24" : "AND al",        # DONE?    # next byte represents and value (in hex), eg. 24 22 > AND al, 0x22  ; 34
    "27" : "DAA",           # DONE
    "29" : "SUB",           # DONE?    # if nexy byte is equal to C6 then: SUB esi, eax
    "2C" : "SUB al",        # DONE?    # next byte represents sub value (in hex), eg. 2C 87 > SUB al, 0x87  ; 135
    "2F" : "DAS",           # DONE
    "30" : "XOR",           # DONE?    # if next byte is equal to 00 then: XOR byte [eax], al
                            # DONE?    #           -||-        to 4D then: XOR byte [ebp + <value>], cl     where VALUE is the byte after 4D
    "31" : "XOR",           # DONE?    # if next byte is equal to ED then: XOR ebp, ebp
                            # DONE?    #           -||-        to FF then: XOR edi, edi
    "32" : "XOR",           # DONE?    # if next byte is equal to 00 then: XOR al, byte [eax]
                            # DONE?    #           -||-        to 2E then: XOR ch, byte [esi]
    "34" : "XOR",           # DONE?    # next byte represents XOR value: XOR al, <VALUE>
    "40" : "INC eax",       # DONE
    "41" : "INC ecx",       # DONE
    "42" : "INC edx",       # DONE
    "43" : "INC ebx",       # DONE
    "44" : "INC esp",       # DONE
    "45" : "INC ebp",       # DONE
    "46" : "INC esi",       # DONE
    "47" : "INC edi",       # DONE
    "48" : "DEC eax",       # DONE
    "49" : "DEC ecx",       # DONE
    "4A" : "DEC edx",       # DONE
    "4B" : "DEC ebx",       # DONE
    "4C" : "DEC esp",       # DONE
    "4D" : "DEC ebp",       # DONE
    "4E" : "DEC esi",       # DONE
    "4F" : "DEC edi",       # DONE
    "50" : "PUSH eax",      # DONE
    "51" : "PUSH ecx",      # DONE
    "52" : "PUSH edx",      # DONE
    "53" : "PUSH ebx",      # DONE
    "54" : "PUSH esp",      # DONE
    "55" : "PUSH ebp",      # DONE
    "56" : "PUSH esi",      # DONE
    "57" : "PUSH edi",      # DONE
    "58" : "POP eax",       # DONE
    "59" : "POP ecx",       # DONE
    "5A" : "POP edx",       # DONE
    "5B" : "POP ebx",       # DONE
    "5C" : "POP esp",       # DONE
    "5D" : "POP ebp",       # DONE
    "5E" : "POP esi",       # DONE
    "5F" : "POP edi",       # DONE
    "61" : "POPAL",         # DONE     
    "64" : "NOP",           # DONE?    # if next byte is equal to 90 then: NOP
    "65" : "NOP",           # DONE?    # if next byte is equal to 90 then: NOP
    "66" : "NOP",           # DONE?    # if next byte is equal to 90 then: NOP
    "67" : "NOP",           # DONE?    # if next byte is equal to 90 then: NOP
    "68" : "PUSH",          # DONE?    # next 4 bytes represents *string* address, in format: AB CD EF GH -> GH EF CD AB
    "70" : "JO",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 70 0E -> JO <ADDRESS OF THIS INSTRUCTION>+16 (int('0E',16)+2=16) # + logic behind reverse jumps: if 2nd byte>128
    "71" : "JNO",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JNO <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "72" : "JB",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JB <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "73" : "JAE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 71 1A -> JAE <ADDRESS OF THIS INSTRUCTION>+28 (int('1A',16)+2=28) # + logic behind reverse jumps: if 2nd byte>128
    "74" : "JE",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 74 05 -> JE <ADDRESS OF THIS INSTRUCTION>+7 (int('05',16)+2=7)    # + logic behind reverse jumps: if 2nd byte>128
    "75" : "JNE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 75 05 -> JNE <ADDRESS OF THIS INSTRUCTION>+7 (int('05',16)+2=7)   # + logic behind reverse jumps: if 2nd byte>128
    "7E" : "JLE",           # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 7E 2C -> JLE <ADDRESS OF THIS INSTRUCTION>+46 (int('2C',16)+2=46) # + logic behind reverse jumps: if 2nd byte>128
    "7F" : "JG",            # DONE?    # next byte represents how much instructions to jump (+2(dec)). Example: 7F 1D -> JG <ADDRESS OF THIS INSTRUCTION>+31 (int('1D',16)+2=31) # + logic behind reverse jumps: if 2nd byte>128
    "81" : "ADD",           # DONE?    # if next byte is equal to C3 then: ADD ebx, <value> where VALUE is (hexadecimal, and) equal to next for bytes in this format: GH EF CD AB
                            # DONE?    #             -||-      to EC then: SUB esp, <value>                                  -||-
    "83" : "ADD",           # DONE?    # if nexy byte is equal to C2 then: ADD edx, <value>  where VALUE is equal to byte after C2
                            # DONE?    #             -||-      to C7 then: ADD edi, <VALUE>             -||-
                            # DONE?    #             -||-      to C4 then: ADD esp, <VALUE>             -||-
                            # DONE?    #             -||-      to C0 then: ADD eax, <VALUE>             -||-
                            # DONE?    #             -||-      to E4 then: AND esp, <VALUE>             -||-
                            # DONE?    #             -||-      to F8 then: CMP eax, <VALUE>             -||-
                            # DONE?    #             -||-      to 3B then: CMP dword [ebx], <VALUE>     -||-
                            # DONE?    #             -||-      to EC then: SUB esp, <VALUE>             -||-
                            # DONE?    #             -||-      to EA then: SUB edx, <VALUE>             -||-
                            # DONE?    #             -||-      to 08 then: OR dword [eax], <VALUE>      -||-
                            # DONE?    # if next 2 bytes: 45 FC <value> then: ADD dword [var_4h], <value>
                            # DONE?    # if next 2 bytes: 7D 08 <value> then: CMP dword [arg_8h], <value>
    "84" : "TEST",          # DONE?    # if next byte is equal to FF then: TEST bh, bh
                            # DONE?    #           -||-        to FE then: TEST dh, bh
                            # DONE?    #           -||-        to FD then: TEST ch, bh
                            # DONE?    #           -||-        to FC then: TEST ah, bh
                            # DONE?    #           -||-        to FB then: TEST bl, bh
                            # DONE?    #           -||-        to FA then: TEST dl, bh
                            # DONE?    #           -||-        to F9 then: TEST cl, bh
                            # DONE?    #           -||-        to F8 then: TEST al, bh
                            # DONE?    #           -||-        to F7 then: TEST bh, dh
                            # DONE?    #           -||-        to F6 then: TEST dh, dh
                            # DONE?    #           -||-        to F5 then: TEST ch, dh
                            # DONE?    #           -||-        to F4 then: TEST ah, dh
                            # DONE?    #           -||-        to F3 then: TEST bl, dh
                            # DONE?    #           -||-        to F2 then: TEST dl, dh
                            # DONE?    #           -||-        to F1 then: TEST cl, dh
                            # DONE?    #           -||-        to F0 then: TEST al, dh
                            # DONE?    #           -||-        to EF then: TEST bh, ch
                            # DONE?    #           -||-        to EE then: TEST dh, ch
                            # DONE?    #           -||-        to ED then: TEST ch, ch
                            # DONE?    #           -||-        to EC then: TEST ah, ch
                            # DONE?    #           -||-        to EB then: TEST bl, ch
                            # DONE?    #           -||-        to EA then: TEST dl, ch
                            # DONE?    #           -||-        to E9 then: TEST cl, ch
                            # DONE?    #           -||-        to E8 then: TEST al, ch
                            # DONE?    #           -||-        to E7 then: TEST bh, ah
                            # DONE?    #           -||-        to E6 then: TEST dh, ah
                            # DONE?    #           -||-        to E5 then: TEST ch, ah
                            # DONE?    #           -||-        to E4 then: TEST ah, ah
                            # DONE?    #           -||-        to E3 then: TEST bl, ah
                            # DONE?    #           -||-        to E2 then: TEST dl, ah
                            # DONE?    #           -||-        to E1 then: TEST cl, ah
                            # DONE?    #           -||-        to E0 then: TEST al, ah
                            # DONE?    #           -||-        to DF then: TEST bh, bl
                            # DONE?    #           -||-        to DE then: TEST dh, bl
                            # DONE?    #           -||-        to DD then: TEST ch, bl
                            # DONE?    #           -||-        to DC then: TEST ah, bl
                            # DONE?    #           -||-        to DB then: TEST bl, bl
                            # DONE?    #           -||-        to DA then: TEST dl, bl
                            # DONE?    #           -||-        to D9 then: TEST cl, bl
                            # DONE?    #           -||-        to D8 then: TEST al, bl
                            # DONE?    #           -||-        to D7 then: TEST bh, dl
                            # DONE?    #           -||-        to D6 then: TEST dh, dl
                            # DONE?    #           -||-        to D5 then: TEST ch, dl
                            # DONE?    #           -||-        to D4 then: TEST ah, dl
                            # DONE?    #           -||-        to D3 then: TEST bl, dl
                            # DONE?    #           -||-        to D2 then: TEST dl, dl
                            # DONE?    #           -||-        to D1 then: TEST cl, dl
                            # DONE?    #           -||-        to D0 then: TEST al, dl
                            # DONE?    #           -||-        to CF then: TEST bh, cl
                            # DONE?    #           -||-        to CE then: TEST dh, cl
                            # DONE?    #           -||-        to CD then: TEST ch, cl
                            # DONE?    #           -||-        to CC then: TEST ah, cl
                            # DONE?    #           -||-        to CB then: TEST bl, cl
                            # DONE?    #           -||-        to CA then: TEST dl, cl
                            # DONE?    #           -||-        to C9 then: TEST cl, cl
                            # DONE?    #           -||-        to C8 then: TEST al, cl
                            # DONE?    #           -||-        to C7 then: TEST bh, al
                            # DONE?    #           -||-        to C6 then: TEST dh, al
                            # DONE?    #           -||-        to C5 then: TEST ch, al
                            # DONE?    #           -||-        to C4 then: TEST ah, al
                            # DONE?    #           -||-        to C3 then: TEST bl, al
                            # DONE?    #           -||-        to C2 then: TEST dl, al
                            # DONE?    #           -||-        to C1 then: TEST cl, al
                            # DONE?    #           -||-        to C0 then: TEST al, al
    "85" : "TEST",          # DONE?    # if next byte is equal to FF then: TEST edi, edi
                            # DONE?    #           -||-        to FE then: TEST esi, edi
                            # DONE?    #           -||-        to FD then: TEST ebp, edi
                            # DONE?    #           -||-        to FC then: TEST esp, edi
                            # DONE?    #           -||-        to FB then: TEST ebx, edi
                            # DONE?    #           -||-        to FA then: TEST edx, edi
                            # DONE?    #           -||-        to F9 then: TEST ecx, edi
                            # DONE?    #           -||-        to F8 then: TEST eax, edi
                            # DONE?    #           -||-        to F7 then: TEST edi, esi
                            # DONE?    #           -||-        to F6 then: TEST esi, esi
                            # DONE?    #           -||-        to F5 then: TEST ebp, esi
                            # DONE?    #           -||-        to F4 then: TEST esp, esi
                            # DONE?    #           -||-        to F3 then: TEST ebx, esi
                            # DONE?    #           -||-        to F2 then: TEST edx, esi
                            # DONE?    #           -||-        to F1 then: TEST ecx, esi
                            # DONE?    #           -||-        to F0 then: TEST eax, esi
                            # DONE?    #           -||-        to EF then: TEST edi, ebp
                            # DONE?    #           -||-        to EE then: TEST esi, ebp
                            # DONE?    #           -||-        to ED then: TEST ebp, ebp
                            # DONE?    #           -||-        to EC then: TEST esp, ebp
                            # DONE?    #           -||-        to EB then: TEST ebx, ebp
                            # DONE?    #           -||-        to EA then: TEST edx, ebp
                            # DONE?    #           -||-        to E9 then: TEST ecx, ebp
                            # DONE?    #           -||-        to E8 then: TEST eax, ebp
                            # DONE?    #           -||-        to E7 then: TEST edi, esp
                            # DONE?    #           -||-        to E6 then: TEST esi, esp
                            # DONE?    #           -||-        to E5 then: TEST ebp, esp
                            # DONE?    #           -||-        to E4 then: TEST esp, esp
                            # DONE?    #           -||-        to E3 then: TEST ebx, esp
                            # DONE?    #           -||-        to E2 then: TEST edx, esp
                            # DONE?    #           -||-        to E1 then: TEST ecx, esp
                            # DONE?    #           -||-        to E0 then: TEST eax, esp
                            # DONE?    #           -||-        to DF then: TEST edi, ebx
                            # DONE?    #           -||-        to DE then: TEST esi, ebx
                            # DONE?    #           -||-        to DD then: TEST ebp, ebx
                            # DONE?    #           -||-        to DC then: TEST esp, ebx
                            # DONE?    #           -||-        to DB then: TEST ebx, ebx
                            # DONE?    #           -||-        to DA then: TEST edx, ebx
                            # DONE?    #           -||-        to D9 then: TEST ecx, ebx
                            # DONE?    #           -||-        to D8 then: TEST eax, ebx
                            # DONE?    #           -||-        to D7 then: TEST edi, edx
                            # DONE?    #           -||-        to D6 then: TEST esi, edx
                            # DONE?    #           -||-        to D5 then: TEST ebp, edx
                            # DONE?    #           -||-        to D4 then: TEST esp, edx
                            # DONE?    #           -||-        to D3 then: TEST ebx, edx
                            # DONE?    #           -||-        to D2 then: TEST edx, edx
                            # DONE?    #           -||-        to D1 then: TEST ecx, edx
                            # DONE?    #           -||-        to D0 then: TEST eax, edx
                            # DONE?    #           -||-        to CF then: TEST edi, ecx
                            # DONE?    #           -||-        to CE then: TEST esi, ecx
                            # DONE?    #           -||-        to CD then: TEST ebp, ecx
                            # DONE?    #           -||-        to CC then: TEST esp, ecx
                            # DONE?    #           -||-        to CB then: TEST ebx, ecx
                            # DONE?    #           -||-        to CA then: TEST edx, ecx
                            # DONE?    #           -||-        to C9 then: TEST ecx, ecx
                            # DONE?    #           -||-        to C8 then: TEST eax, ecx
                            # DONE?    #           -||-        to C7 then: TEST edi, eax
                            # DONE?    #           -||-        to C6 then: TEST esi, eax
                            # DONE?    #           -||-        to C5 then: TEST ebp, eax
                            # DONE?    #           -||-        to C4 then: TEST esp, eax
                            # DONE?    #           -||-        to C3 then: TEST ebx, eax
                            # DONE?    #           -||-        to C2 then: TEST edx, eax
                            # DONE?    #           -||-        to C1 then: TEST ecx, eax
                            # DONE?    #           -||-        to C0 then: TEST eax, eax
    "89" : "MOV",           # DONE?    # if next byte is equal to C0 then: MOV eax, eax
                            # DONE?    #             -||-      to C1 then: MOV ecx, eax
                            # DONE?    #             -||-      to C2 then: MOV edx, eax
                            # DONE?    #             -||-      to C3 then: MOV ebx, eax
                            # DONE?    #             -||-      to C4 then: MOV esp, eax
                            # DONE?    #             -||-      to C5 then: MOV ebp, eax
                            # DONE?    #             -||-      to C6 then: MOV esi, eax
                            # DONE?    #             -||-      to C7 then: MOV edi, eax
                            # DONE?    #             -||-      to C8 then: MOV eax, ecx
                            # DONE?    #             -||-      to C9 then: MOV ecx, ecx
                            # DONE?    #             -||-      to CA then: MOV edx, ecx
                            # DONE?    #             -||-      to CB then: MOV ebx, ecx
                            # DONE?    #             -||-      to CC then: MOV esp, ecx
                            # DONE?    #             -||-      to CD then: MOV ebp, ecx
                            # DONE?    #             -||-      to CE then: MOV esi, ecx
                            # DONE?    #             -||-      to CF then: MOV edi, ecx
                            # DONE?    #             -||-      to D0 then: MOV eax, edx
                            # DONE?    #             -||-      to D1 then: MOV ecx, edx
                            # DONE?    #             -||-      to D2 then: MOV edx, edx
                            # DONE?    #             -||-      to D3 then: MOV ebx, edx
                            # DONE?    #             -||-      to D4 then: MOV esp, edx
                            # DONE?    #             -||-      to D5 then: MOV ebp, edx
                            # DONE?    #             -||-      to D6 then: MOV esi, edx
                            # DONE?    #             -||-      to D7 then: MOV edi, edx
                            # DONE?    #             -||-      to D8 then: MOV eax, ebx
                            # DONE?    #             -||-      to D9 then: MOV ecx, ebx
                            # DONE?    #             -||-      to DA then: MOV edx, ebx
                            # DONE?    #             -||-      to DB then: MOV ebx, ebx
                            # DONE?    #             -||-      to DC then: MOV esp, ebx
                            # DONE?    #             -||-      to DD then: MOV ebp, ebx
                            # DONE?    #             -||-      to DE then: MOV esi, ebx
                            # DONE?    #             -||-      to DF then: MOV edi, ebx
                            # DONE?    #             -||-      to E0 then: MOV eax, esp
                            # DONE?    #             -||-      to E1 then: MOV ecx, esp
                            # DONE?    #             -||-      to E2 then: MOV edx, esp
                            # DONE?    #             -||-      to E3 then: MOV ebx, esp
                            # DONE?    #             -||-      to E4 then: MOV esp, esp
                            # DONE?    #             -||-      to E5 then: MOV ebp, esp
                            # DONE?    #             -||-      to E6 then: MOV esi, esp
                            # DONE?    #             -||-      to E7 then: MOV edi, esp
                            # DONE?    #             -||-      to E8 then: MOV eax, ebp
                            # DONE?    #             -||-      to E9 then: MOV ecx, ebp
                            # DONE?    #             -||-      to EA then: MOV edx, ebp
                            # DONE?    #             -||-      to EB then: MOV ebx, ebp
                            # DONE?    #             -||-      to EC then: MOV esp, ebp
                            # DONE?    #             -||-      to ED then: MOV ebp, ebp
                            # DONE?    #             -||-      to EE then: MOV esi, ebp
                            # DONE?    #             -||-      to EF then: MOV edi, ebp
                            # DONE?    #             -||-      to F0 then: MOV eax, esi
                            # DONE?    #             -||-      to F1 then: MOV ecx, esi
                            # DONE?    #             -||-      to F2 then: MOV edx, esi
                            # DONE?    #             -||-      to F3 then: MOV ebx, esi
                            # DONE?    #             -||-      to F4 then: MOV esp, esi
                            # DONE?    #             -||-      to F5 then: MOV ebp, esi
                            # DONE?    #             -||-      to F6 then: MOV esi, esi
                            # DONE?    #             -||-      to F7 then: MOV edi, esi
                            # DONE?    #             -||-      to F8 then: MOV eax, edi
                            # DONE?    #             -||-      to F9 then: MOV ecx, edi
                            # DONE?    #             -||-      to FA then: MOV edx, edi
                            # DONE?    #             -||-      to FB then: MOV ebx, edi
                            # PENDING  #             -||-      to FC then: MOV esp, edi
                            # PENDING  #             -||-      to FD then: MOV ebp, edi
                            # PENDING  #             -||-      to FE then: MOV esi, edi
                            # PENDING  #             -||-      to FF then: MOV edi, edi
    "8B" : "MOV",           # DONE?    # if next byte is equal to 1C and next byte equal to 24 then: MOV ebx, dword [esp]
                            # DONE?    #             -||-      to 10 then: MOV edx, dword [eax]
                            # DONE?    #             -||-      to 55 then: MOV edx, dword [var_4h]
                            # DONE?    #             -||-      to 45 then: MOV eax, dword [arg_8h]
                            # DONE?    #             -||-      to 4D then: MOV ecx, dword [var_4h]
                            # DONE?    #             -||-      to 00 then: MOV eax, dword [eax]
                            # DONE?    #             -||-      to 6C then: MOV ebp, dword [arg_4h]
                            # DONE?    #             -||-      to 43 then: MOV eax, dword [ebx + <VALUE>] where <VALUE> is equal to byte after 43
                            # PENDING  #             -||-      to 83 then: NEED TO ADD MORE INFO! -------------------------------
    "90" : "NOP",           # DONE
    "98" : "CWDE",          # DONE
    "99" : "CDQ",           # DONE
    "B8" : "MOV eax",       # PENDING  # next byte represents MOV value / if 4 next bytes are not instructions, then those bytes represent an adress in format: B8 AB CD EF GH > MOV eax, 0xGHEFCDAB
    "BA" : "MOV edx",       # DONE?    # next byte represents MOV value
    "C3" : "RET",           # DONE
    "C9" : "LEAVE",         # DONE
    "CF" : "IRETD",         # DONE
    "E4" : "IN",            # DONE?    # next byte represents value: IN al, <VALUE>
    "E8" : "CALL",          # PENDING  # need to add more info
    "EC" : "IN al, dx",     # DONE
    "ED" : "IN eax, dx",    # DONE
    "EE" : "OUT dx, al",    # DONE
    "EF" : "OUT dx, eax",   # DONE
    "F3" : "RET",           # DONE?    # if next byte is equal to C3 then: RET
    "F6" : "NOT",           # DONE?    # if next byte is equal to FF then: IDIV bh
                            # DONE?    #           -||-        to FE then: IDIV dh
                            # DONE?    #           -||-        to FD then: IDIV ch
                            # DONE?    #           -||-        to FC then: IDIV ah
                            # DONE?    #           -||-        to FB then: IDIV bl
                            # DONE?    #           -||-        to FA then: IDIV dl
                            # DONE?    #           -||-        to F9 then: IDIV cl
                            # DONE?    #           -||-        to F8 then: IDIV al
                            # DONE?    #           -||-        to F7 then: DIV bh
                            # DONE?    #           -||-        to F6 then: DIV dh
                            # DONE?    #           -||-        to F5 then: DIV ch
                            # DONE?    #           -||-        to F4 then: DIV ah
                            # DONE?    #           -||-        to F3 then: DIV bl
                            # DONE?    #           -||-        to F2 then: DIV dl
                            # DONE?    #           -||-        to F1 then: DIV cl
                            # DONE?    #           -||-        to F0 then: DIV al
                            # DONE?    #           -||-        to EF then: IMUL bh
                            # DONE?    #           -||-        to EE then: IMUL dh
                            # DONE?    #           -||-        to ED then: IMUL ch
                            # DONE?    #           -||-        to EC then: IMUL ah
                            # DONE?    #           -||-        to EB then: IMUL bl
                            # DONE?    #           -||-        to EA then: IMUL dl
                            # DONE?    #           -||-        to E9 then: IMUL cl
                            # DONE?    #           -||-        to E8 then: IMUL al
                            # DONE?    #           -||-        to E7 then: MUL bh
                            # DONE?    #           -||-        to E6 then: MUL dh
                            # DONE?    #           -||-        to E5 then: MUL ch
                            # DONE?    #           -||-        to E4 then: MUL ah
                            # DONE?    #           -||-        to E3 then: MUL bl
                            # DONE?    #           -||-        to E2 then: MUL dl
                            # DONE?    #           -||-        to E1 then: MUL cl
                            # DONE?    #           -||-        to E0 then: MUL al
                            # DONE?    #           -||-        to DF then: NEG bh
                            # DONE?    #           -||-        to DE then: NEG dh
                            # DONE?    #           -||-        to DD then: NEG ch
                            # DONE?    #           -||-        to DC then: NEG ah
                            # DONE?    #           -||-        to DB then: NEG bl
                            # DONE?    #           -||-        to DA then: NEG dl
                            # DONE?    #           -||-        to D9 then: NEG cl
                            # DONE?    #           -||-        to D8 then: NEG al
                            # DONE?    #           -||-        to D7 then: NOT bh
                            # DONE?    #           -||-        to D6 then: NOT dh
                            # DONE?    #           -||-        to D5 then: NOT ch
                            # DONE?    #           -||-        to D4 then: NOT ah
                            # DONE?    #           -||-        to D3 then: NOT bl
                            # DONE?    #           -||-        to D2 then: NOT dl
                            # DONE?    #           -||-        to D1 then: NOT cl
                            # DONE?    #           -||-        to D0 then: NOT al
    "F7" : "NOT",           # DONE?    # if next byte is equal to FF then: IDIV edi
                            # DONE?    #           -||-        to FE then: IDIV esi
                            # DONE?    #           -||-        to FD then: IDIV ebp
                            # DONE?    #           -||-        to FC then: IDIV esp
                            # DONE?    #           -||-        to FB then: IDIV ebx
                            # DONE?    #           -||-        to FA then: IDIV edx
                            # DONE?    #           -||-        to F9 then: IDIV ecx
                            # DONE?    #           -||-        to F8 then: IDIV eax
                            # DONE?    #           -||-        to F7 then: DIV edi
                            # DONE?    #           -||-        to F6 then: DIV esi
                            # DONE?    #           -||-        to F5 then: DIV ebp
                            # DONE?    #           -||-        to F4 then: DIV esp
                            # DONE?    #           -||-        to F3 then: DIV ebx
                            # DONE?    #           -||-        to F2 then: DIV edx
                            # DONE?    #           -||-        to F1 then: DIV ecx
                            # DONE?    #           -||-        to F0 then: DIV eax
                            # DONE?    #           -||-        to EF then: IMUL edi
                            # DONE?    #           -||-        to EE then: IMUL esi
                            # DONE?    #           -||-        to ED then: IMUL ebp
                            # DONE?    #           -||-        to EC then: IMUL esp
                            # DONE?    #           -||-        to EB then: IMUL ebx
                            # DONE?    #           -||-        to EA then: IMUL edx
                            # DONE?    #           -||-        to E9 then: IMUL ecx
                            # DONE?    #           -||-        to E8 then: IMUL eax
                            # DONE?    #           -||-        to E7 then: MUL edi
                            # DONE?    #           -||-        to E6 then: MUL esi
                            # DONE?    #           -||-        to E5 then: MUL ebp
                            # DONE?    #           -||-        to E4 then: MUL esp
                            # DONE?    #           -||-        to E3 then: MUL ebx
                            # DONE?    #           -||-        to E2 then: MUL edx
                            # DONE?    #           -||-        to E1 then: MUL ecx
                            # DONE?    #           -||-        to E0 then: MUL eax
                            # DONE?    #           -||-        to DF then: NEG edi
                            # DONE?    #           -||-        to DE then: NEG esi
                            # DONE?    #           -||-        to DD then: NEG ebp
                            # DONE?    #           -||-        to DC then: NEG esp
                            # DONE?    #           -||-        to DB then: NEG ebx
                            # DONE?    #           -||-        to DA then: NEG edx
                            # DONE?    #           -||-        to D9 then: NEG ecx
                            # DONE?    #           -||-        to D8 then: NEG eax
                            # DONE?    #           -||-        to D7 then: NOT edi
                            # DONE?    #           -||-        to D6 then: NOT esi
                            # DONE?    #           -||-        to D5 then: NOT ebp
                            # DONE?    #           -||-        to D4 then: NOT esp
                            # DONE?    #           -||-        to D3 then: NOT ebx
                            # DONE?    #           -||-        to D2 then: NOT edx
                            # DONE?    #           -||-        to D1 then: NOT ecx
                            # DONE?    #           -||-        to D0 then: NOT eax
    "F8" : "CLC",           # DONE
    "FF" : "CALL",          # DONE?    # if next byte is equal to d0 then: CALL eax    # FF is also associated with JMP, INC, need to add more info
                            # DONE?    #             -||-      to d1 then: CALL ecx
                            # DONE?    #             -||-      to d2 then: CALL edx
                            # DONE?    #             -||-      to d3 then: CALL ebx
                            # DONE?    #             -||-      to d4 then: CALL esp
                            # DONE?    #             -||-      to d5 then: CALL ebp
                            # DONE?    #             -||-      to d6 then: CALL esi
                            # DONE?    #             -||-      to d7 then: CALL edi
}

x860Fopcodes = {
    "84" : "JE",            # PENDING  # need to add more info
    "A0" : "PUSH fs",       # DONE?
    "A1" : "POP fs",        # DONE?
    "A8" : "PUSH gs",       # DONE?
    "A9" : "POP gs",        # DONE?
}
