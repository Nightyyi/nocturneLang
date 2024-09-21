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
    
    
    new_ = ""
    line_counter=0
    for index, line in enumerate(flines):
        linestr = line.split()
        if linestr[0] == "#call":
            line_counter+=1
            other_line = flines[index+1].split()
            print(linestr)
            other_line.pop(0)
            start_ = 0
            for i in range(0,64):
                check = "r"+str(i)
                if check in variables:
                    v_start = variables_start[variables.index( check )]
                    v_end = variables_end[variables.index( check )]
                    if check in other_line and (v_start < line_counter < v_end):
                        new_+= "ld r61 "+ str(i-start_) + "\n"
                        start_ = i
                        new_+= "add r61 r62 r62\n"
                        new_+= "wr r" + str(i) + " r62\n"
            new_+= "ld r61 "+ str(start_) + "\n"
            new_+= "sub r61 r62 r62\n"
            new_+= "ld r61 64\n"
            new_+= "sub r61 r62 r62\n"
            new_+= "#jump "+ linestr[2] + "\n"
            new_+= "ld " + linestr[1] + " r60\n"
            start_ = 0
            for i in range(0,64):
                check = "r"+str(i)
                if check in variables:
                    v_start = variables_start[variables.index( check )]
                    v_end = variables_end[variables.index( check )]
                    if check in other_line and (v_start < line_counter < v_end):
                        new_+= "ld r61 "+ str(i-start_) + "\n"
                        start_ = i
                        new_+= "add r61 r62 r62\n"
                        new_+= "rd r" + str(i) + " r62\n"
            new_+= "ld r61 "+ str(start_) + "\n"
            new_+= "sub r61 r62 r62\n"
        elif linestr[0][0] == "#":
            print("idk")
            line_counter+=1
        else:
            new_+=line+"\n"
            line_counter+=1

    file = open("compileds\\"+function, "w")
    file.write(new_)
    file.close()    
