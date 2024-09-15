file = open("IR.txt","r")
filestr = file.read()
file.close()


strlist = []
characc = ""
for char in filestr:
    if char != "\n":
        characc += char
    else:
        strlist.append(characc)
        characc = ""

vars = []
varsmin = []
varsmax = []
for index, line in enumerate(strlist):
    linestr = line.split()
    if linestr[0] == "ld":
        linestr[1] = linestr[1].replace('-', '')
        if not linestr[1].isnumeric():
            if linestr[1] in vars:
                indexvar = vars.index(linestr[1])
                if varsmax[indexvar] < index:
                    varsmax[indexvar] = index
            else:
                vars.append(linestr[1])
                varsmax.append(index)
                varsmin.append(index)
    else:
        for i in range(1,len(linestr)):
            linestr[i] = linestr[i].replace('-', '')
            if not linestr[i].isnumeric():
                print(linestr[i])
                if linestr[i] in vars:
                    indexvar = vars.index(linestr[i])
                    if varsmax[indexvar] < index:
                        varsmax[indexvar] = index
                else:

                    vars.append(linestr[i])
                    varsmax.append(index)
                    varsmin.append(index)
print(vars)
print(varsmin)
print(varsmax)


file = open("IRFreed.txt","w")
for i in range(0,len(varsmax)):
    n = len(varsmax)-i
    strinsert = "|free " + vars[n-1]
    strlist.insert(varsmax[n-1]+1,strinsert)

stracclist = ""
for i in range(0,len(strlist)):
    stracclist += strlist[i] + "\n"
file.write(stracclist)
file.close()
