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

print(functions)


for function in functions:
    file = open("funcs\\"+function, "r")
    flistch = file.read()
    file.close()    
    flines = []
    acc = ""

    for ch in flistch:
        if ch == '\n':
            flines.append(acc)
            acc = ""
        else: 
            acc+=ch
    
    variables = []
    variables_start = []
    variables_end = []

    for index, line in enumerate(flines):
        linestr = line.split()
        for i in range(1,len(linestr)):
            individual_variable = linestr[i]
            first_character = individual_variable[0]
            if first_character != '*':
                if not individual_variable.isnumeric():
                    if not individual_variable in variables:
                        variables.append(individual_variable)
                        variables_start.append(index)
                        variables_end.append(index)
                    else: 
                        variables_end[variables.index(individual_variable)] = index

    print(variables,variables_start,variables_end)
    
    alloc_reg = [0] * 64
    new_ = ""
    for index, line in enumerate(flines):
        linestr = line.split()
        new_line = linestr 
        for i in range(1,len(linestr)):
            individual_variable = linestr[i]
            first_character = individual_variable[0]
            if first_character != '*':
                if not individual_variable.isnumeric():
                    if not individual_variable in alloc_reg:
                        for rin,check in enumerate(alloc_reg):
                            if check == 0:
                                alloc_reg[rin] = individual_variable
                                break
                            
                        new_line[i] = "r"+str(alloc_reg.index(individual_variable))
                    else:
                        new_line[i] = "r"+str(alloc_reg.index(individual_variable))
                        for alloc_var in alloc_reg:
                            if alloc_var != 0:
                                if not variables_end[(variables.index(alloc_var))] >= index:
                                    alloc_reg[(alloc_reg.index(alloc_var))] = 0

        for string in new_line:
            new_ = new_ + string + " "
        new_ += "\n"
        if linestr[0] == "#call":
            regs_c = []
            new_ += "# "
            for i in range(1,len(new_line)):
                regs_c.append(new_line[i])
                
            
            for i in range(0,len(alloc_reg)):
                if (not alloc_reg[i] in regs_c) and alloc_reg[i] != 0:
                    new_+= "r" + str(i) + " "
            new_ += "\n"
    print(new_)

    file = open("funcs\\"+function, "w")
    file.write(new_)
    file.close()    
