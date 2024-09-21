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
    file = open("compileds\\"+function, "r")
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
        if linestr[0] == "retr":
            new_+="ld r60 "+ linestr[1] + "\n" 
            new_+="ld r57 57\n" 
            new_+="clr r57\n"
            new_+="ld r61 64\n"
            new_+="sub r61 r62 r62\n"
            new_+="j r63\n"
        else:
            new_+=line+"\n"

    file = open("compileds\\"+function, "w")
    file.write(new_)
    file.close()    
