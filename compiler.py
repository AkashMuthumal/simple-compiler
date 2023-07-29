# Created by Akash

x = "undefined"

type1 = {"add":2, "sub":3, "and":4, "or":5, "mult":11}
type2 = {"loadi":0}
type3 = {"sll":x, "srl":x, "sra":x, "ror":x}
type4 = {"bne":x, "beq":7}
type5 = {"j":6}
type6 = {"mov":1, "lwd":8}
type7 = {"swi":11}
type8 = {"swd":10}
type9 = {"lwi":9}

#   swi ok
#   lwi ok
#   swd ok
#   lwd ok

instruction_set = ["loadi 1 0x2",
                   "loadi 2 0x5",
                   "lwi 3 0x2"]

'''
instruction_set = ["loadi 1 0x2",
                   "loadi 2 0x3",
                   "swi 2 0x5",
                   "lwi 6 0x5"]'''


'''
"swd 2 1",   # write value from register 2 (RT) to the memory at address given in register 1
"lwd 6 1",  # Read memory at address given in register 1 (RS)and store result in register 6 (RD)
"loadi 2 0x5",
"swi 2 0x5",     # swi 2 0x8C : write value from register 2 (RT) to the memory at address 0x8C (IMM).
"lwi 0x5 1"]       # lwi 4 0x1F : Read memory at address 0x1F (IMM) and store result it in register 4
'''

for i in instruction_set:

    instruction = i.split()

    if(instruction[0] in type1.keys()):
        print(format(int(instruction[3]), '08b'), end=" ")
        print(format(int(instruction[2]), '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(type1[instruction[0]], '08b'), end=" ")
        

    if(instruction[0] in type2.keys()):
        print(format(eval(instruction[2]), '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(type2[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type3.keys()):
        if(instruction[0]=="srl"):
            print(format(eval(instruction[3])+128, '08b'), end=" ")
            print(format(int(instruction[2]), '08b'), end=" ")
            print(format(int(instruction[1]), '08b'), end=" ")
            print(format(type3[instruction[0]], '08b'), end=" ")

        else:
            print(format(eval(instruction[3]), '08b'), end=" ")
            print(format(int(instruction[2]), '08b'), end=" ")
            print(format(int(instruction[1]), '08b'), end=" ")
            print(format(type3[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type4.keys()):
        print(format(int(instruction[3]), '08b'), end=" ")
        print(format(int(instruction[2]), '08b'), end=" ")
        print(format(eval(instruction[1]), '08b'), end=" ")
        print(format(type4[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type5.keys()):
        print(format(0, '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(eval(instruction[1]), '08b'), end=" ")
        print(format(type5[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type6.keys()):
        print(format(int(instruction[2]), '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(type6[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type7.keys()):
        print(format(eval(instruction[2]), '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(type7[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type8.keys()):
        print(format(int(instruction[2]), '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(type8[instruction[0]], '08b'), end=" ")

    if(instruction[0] in type9.keys()):
        print(format(eval(instruction[2]), '08b'), end=" ")
        print(format(0, '08b'), end=" ")
        print(format(int(instruction[1]), '08b'), end=" ")
        print(format(type9[instruction[0]], '08b'), end=" ")

    print()
    

#    mult 4 1 2 (multiply value in register 1 by value in register 2, and place the result in register 4)
#    sll 4 1 0x02 (apply logical shift left 2 times on value in register 1, and place the result in register 4)
#    srl 4 1 0x02 (apply logical shift right 2 times on value in register 1, and place the result in register 4)
#    sra 4 1 0x02 (apply arithmetic shift right 2 times on value in register 1, and place the result in register 4)
#    ror 4 1 0x02 (apply rotate right 2 times on value in register 1, and place the result in register 4)
#    bne 0x02 1 2
#    add 4 1 2 (add value in register 2 to value in register 1, and place the result in register 4)
#    sub 4 1 2 (subtract value in register 2 from the value in register 1, and place the result in register 4)
#    and 4 1 2 (perform bit-wise AND on values in registers 1 and 2, and place the result in register 4)
#    or 4 1 2 (perform bit-wise OR on values in registers 1 and 2, and place the result in register 4)
#    j 0x02 
#    beq 0xFE 1 2 
#    mov 4 1 (copy the value in register 1 to register 4. Ignore bits 15-8)
#    loadi 4 0xFF (load the immediate value 0xFF to register 4. Ignore bits 15-8)
#   lwd 4 2 :Read memory at address given in register 2 (RS)and store result in register 4 (RD). Ignore bits 15-8
#   lwi 4 0x1F : Read memory at address 0x1F (IMM) and store result it in register 4 (RD). Ignore bits 15-8
#   swd 2 3 :write value from register 2 (RT) to the memory at address given in register 3 (RS). Ignore bits 23-16
#   swi 2 0x8C : write value from register 2 (RT) to the memory at address 0x8C (IMM). Ignore bits 23-16
