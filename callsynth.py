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
    
    new_ = ""
    for index, line in enumerate(flines):
        linestr = line.split()
        if linestr[0] == "#call":
            other_line = flines[index+1].split()
            other_line.pop(0)
            start_ = 0
            for i in range(0,64):
                check = "r"+str(i)
                if check in other_line:
                    new_+= "ld r61 "+ str(i-start_) + "\n"
                    start_ = i
                    new_+= "add r61 r62 r62\n"
                    new_+= "wr r" + str(i) + " r62\n"
            new_+= "#jump "+ linestr[2] + "\n"
            new_+= "ld " + linestr[1] + " r60\n"
            for i in range(0,64):
                check = "r"+str(i)
                if check in other_line:
                    start_ = i
                    new_+= "add r61 r62 r62\n"
                    new_+= "rd r" + str(i) + " r62\n"
        elif linestr[0][0] == "#":
            print("idk")
        else:
            new_+=line+"\n"

    file = open("compileds\\"+function, "w")
    file.write(new_)
    file.close()    
