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

compiledall = ""
linestarts = []
funcnames = []
lines = 0
for function in functions:
    file = open("compileds\\"+function, "r")
    flistch = file.read()
    linestarts.append(lines)
    for ch in flistch:
        if ch == "\n":
            lines+=1

    funcnames.append(function.split(".")[0])
    compiledall+= flistch + "end\n"
    file.close()    
    
file = open("built", "w")
file.write(compiledall)
file.close()    



lines = []
acc = ""
for ch in compiledall:
    if ch == '\n':
        lines.append(acc)
        acc = ""
    else: 
        acc+=ch

comp = ""
lines_extra = 0
for line in lines:
    line_s = line.split()
    if line_s[0] == "#jump":
        function_name = line_s[1][1:]
        lines_extra+= 8
        jmpval = linestarts[funcnames.index(function_name)] + 1 + lines_extra
        comp+="gad r63\n"
        comp+="ld r61 4\n"
        comp+="add r61 r63 r63" + "\n"
        comp+="ld r61 "+ str(jmpval) + "\n"
        comp+="b r61" + "\n"
        comp+="ld r61 1\n"
        comp+="add r61 r62 r62" + "\n"
        comp+="rd r63 r62\n"
        comp+="sub r61 r62 r62" + "\n"
    else:
        comp+=line+"\n"
print(comp)
file = open("built", "w")
file.write(comp)
file.close()    
