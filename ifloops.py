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
    mode = ""
    mode2 = ""
    mode3 = ""
    new_list = []
    index_if = 0
    index_loop = 0
    index_loopz = 0
    ii = 0
    see_list = []
    for index, line in enumerate(flines):
        linestr = line.split()
        if linestr[0] == "bnz":
            mode = "if"
            new_list.append(linestr[0] +" "+ linestr[1] + " r63")
            ii = len(new_list)-1
            index_if = ii
        elif linestr[0] == "bz":
            mode3 = "if2"
            new_list.append(linestr[0] +" "+ linestr[1] + " r63")
            ii = len(new_list)-1
            index_loopz = ii
        elif linestr[0] == "openloop":
            mode2 = "loop"
            index_loop = ii
        elif linestr[0] == "close" and mode == "if":
            mode = ""
            print(ii, index_if)
            for iii in new_list:
                print(iii)
            print("-------")
            ii = len(new_list)
            new_list.insert(index_if, "ld r63 " + str(ii-index_if))
        elif linestr[0] == "close":

            if mode == "if":
                mode = ""
                print(ii)
                ii = len(new_list)
                new_list.insert(index_if, "ld r63 " + str(index_loop-ii))
            elif mode3 == "if2":
                mode3 = ""
                print(ii)
                ii = len(new_list)+1
                new_list.insert(index_loopz, "ld r63 " + str(ii))
            elif mode2 == "loop":
                mode2 = ""
                ii = len(new_list)+1
                new_list.append("ldn r63 " + str(index_loop-ii))
                new_list.append("b r63 " )

        else:
            new_list.append(line)
            see_list.append(line)
        ii = len(new_list)-1
    print(new_list)
    new_= ""
    for i in new_list:
        new_+=i+"\n"
    for i in see_list:
        print(i)
    file = open("funcs\\"+function, "w")
    file.write(new_)
    file.close()    
