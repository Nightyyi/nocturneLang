
def int_to_bin(integer_value,padding):
    new_string = ""
    integer_value = int(integer_value)
    divider = 1
    i = 0
    while (int(integer_value)//divider > 0 and i < padding):
        if (integer_value//divider % 2 == 1):
            new_string = '1' + new_string
        else:
            new_string = '0' + new_string
        i+=1
        divider*=2

    new_string = "0" * (padding-i) + new_string
    return new_string
def assemble(name):
    file = open("funclist.txt", "r")
    strf = file.read()
    file.close()
    functions = []
    acc = ""
    for ch in strf:
        if ch == '\n':
            functions.append(acc)
            acc = ""
        else: 
            acc+=ch

    for function in functions:
        file = open("compileds\\"+function, "r")
        fcomp = file.read()
        file.close()
        acc = ""
        lines = []
        for ch in fcomp:
            if ch == '\n':
                lines.append(acc)
                acc = ""
            else: 
                acc+=ch
        print(lines)
        
        new_lines = []
        for line_ns in lines:
            inst_add = ""
            line = line_ns.split()
            instruction = line[0]
            print(line)
            if   instruction == "ld":
                list_o_nums = "0123456789"
                if line[2][0] in list_o_nums :
                    inst_add = "0000001" + "0"*3 + int_to_bin(line[1][1:],6) + int_to_bin(line[2][0:],16)                     
                    new_lines.append(inst_add +"\n")
                else:
                    inst_add = "0000011" + "0"*3 + int_to_bin(line[1][1:],6) + int_to_bin(line[2][1:],16) 
                    new_lines.append(inst_add +"\n")

            elif instruction == "add":
                    inst_add = "0000010" + "0000000"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "sub":
                    inst_add = "0000010" + "0000001"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "mul":
                    inst_add = "0000010" + "0001101"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "div":
                    inst_add = "0000010" + "0001110"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")


            elif instruction == "xor":
                    inst_add = "0000010" + "0000010"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "or":
                    inst_add = "0000010" + "0000011"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "and":
                    inst_add = "0000010" + "0000100"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")


            elif instruction == "mrtn":
                    inst_add = "0000010" + "0001010"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6)
                    new_lines.append(inst_add +"\n")
            elif instruction == "lsht":
                    inst_add = "0000010" + "0000101"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            elif instruction == "rsht":
                    inst_add = "0000010" + "0000110"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")

            elif instruction == "rsht":
                    inst_add = "0000010" + "0000110"+ int_to_bin(line[3][1:],6) + int_to_bin(line[2][1:],6) + int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")

            elif instruction == "wr":
                    inst_add = "0000100" + "0" * 3 +  int_to_bin(line[1][1:],6) + int_to_bin(line[2][1:],16) 
                    new_lines.append(inst_add +"\n")

            elif instruction == "rd":
                    inst_add = "0000101" + "0" * 3 +  int_to_bin(line[1][1:],6) + int_to_bin(line[2][1:],16) 
                    new_lines.append(inst_add +"\n")
                
            elif instruction == "b":
                    inst_add = "0000110" + "0" * 19 +  int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            
            elif instruction == "bz":
                    inst_add = "0000111" + "0" * 3 +  int_to_bin(line[2][1:],6) +  int_to_bin(line[1][1:],16)
                    new_lines.append(inst_add +"\n")
            
            elif instruction == "bnz":
                    inst_add = "0001000" + "0" * 3 +  int_to_bin(line[2][1:],6) +  int_to_bin(line[1][1:],16)
                    new_lines.append(inst_add +"\n")
            
            elif instruction == "clr":
                    inst_add = "0001100" + "0" * 19 +  int_to_bin(line[1][1:],6) 
                    new_lines.append(inst_add +"\n")
            
            else:
                new_lines.append("/ "+line_ns+" \\")

        new_ = ""
        print(new_lines)
        for i in new_lines:
            incrementor = 0
            new_line_acc = ""
            for ii in i:
                incrementor +=1
                if ii != ' ' and ii != "\n":
                    new_line_acc+=ii
                if incrementor >= 4:
                    incrementor = 0
                    new_line_acc+=" "
            new_ += new_line_acc + "\n"

        file = open("assembled\\"+function, "w")
        file.write(new_)
        file.close() 

assemble("hi")
