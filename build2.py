
file = open("built", "r")

strf = file.read()
file.close()

lines = []
acc = ""
for ch in strf:
    if ch == '\n':
        functions.append(acc)
        acc = ""
    else: 
        acc+=ch

comp = ""
for line in lines:
    line_s = line.split()
    if line_s[0] == "#jump":
        function_name = line_s[1][1:]
        jmpval = linestarts[funcnames.index(function_name)]
        comp+="j "+ str(jmpval) + "\n"
    else:
        comp+=line+"\n"
print(comp)
file = open("built", "w")
file.write(comp)
file.close()    
