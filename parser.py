def checkin(xlist, possiblevar):
    for i in range(0,len(possiblevar)):
        if not possiblevar[i] in xlist:
            return possiblevar[i]
    return False


def equate(strlist, asmline):
    indx = 0
    vars = []
    possiblevars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s']
    strcode = ""
    print(strlist)
    if len(strlist) == 1:
        return "", strlist[0], 1

    for i in range(0,len(strlist)):
        if strlist[i].isnumeric():
            newvar = checkin(vars, possiblevars)
            if newvar == False:
                while (True):
                    print("something went wrong")
            strcode += "ld " + newvar + " " + str(strlist[i]) + "\n"
            strlist[i] = newvar
    for i in range(0,len(strlist)):
        op = False
        if strlist[i] == ' ||': op = True
        if strlist[i] == ' &&': op = True
        if strlist[i] == ' ^^': op = True
        if strlist[i] == ' +': op = True
        if strlist[i] == ' -': op = True
        if strlist[i] == ' *': op = True
        if strlist[i] == ' /': op = True
        if strlist[i] == ' -(': op = True
        if strlist[i] == ' -)': op = True

        if strlist[i] == ' ==': op = True
        if strlist[i] == ' !=': op = True
        if strlist[i] == ' >=': op = True
        if strlist[i] == ' <=': op = True
        if strlist[i] == ' >': op = True
        if strlist[i] == ' <': op = True
        if op == False:
            vars.append(strlist[i])
            strlist[i] = indx
            indx+=1
    parcounter = 0
    linestoadd = 0
    print(vars)
    print(strlist)
    while len(strlist) != 1:
        score = 0
        i = 0
        print(strlist)
        for ii in range(0,len(strlist)):
            char = strlist[ii]
            if char == ' -(':
                parcounter+=1
            if char == ' -)':
                parcounter-=1
            if char == ' >':
                newscore = (parcounter*4)+1 
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' <':
                newscore = (parcounter*4)+1
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' >=':
                newscore = (parcounter*5)+1
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' <=':
                newscore = (parcounter*5)+1
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' !=':
                newscore = (parcounter*5)+1
                if newscore > score:    
                    i = ii              
                    score = newscore    
            if char == ' ==':           
                newscore = (parcounter*5)+1
                if newscore > score:    
                    i = ii              
                    score = newscore    
            if char == ' ||':          
                newscore = (parcounter*5)+2 
                if newscore > score:    
                    i = ii              
                    score = newscore    
            if char == ' ^^':          
                newscore = (parcounter*5)+2
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' &&':          
                newscore = (parcounter*5)+2
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' +':
                newscore = (parcounter*5)+3
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' -':
                newscore = (parcounter*5)+3 
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' *':
                newscore = (parcounter*5)+4
                if newscore > score:
                    i = ii
                    score = newscore
            if char == ' /':
                newscore = (parcounter*5)+4 
                if newscore > score:
                    i = ii
                    score = newscore

        if strlist[i] == ' +': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "add " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' -': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "sub " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' *': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "mul " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' /': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "div " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' ^^': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "xor" + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' ||': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "or " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' ==': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "eq " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' !=': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "neq " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' >=': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "eqmr " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' <=': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "eqls " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' <': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "mrtn " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' >': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "lstn " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        if strlist[i] == ' &&': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "and " + vars[arg1] + " " + vars[arg2] + " " + newarg + "\n"
            linestoadd+=1
            op = True
        
        caught = True
        while caught and (len(strlist) > 1):
            caught = False
            iiii = 0
            while iiii < len(strlist):
                op = False 
                valid = True
                if strlist[iiii] == ' +': op = True
                if strlist[iiii] == ' -': op = True
                if strlist[iiii] == ' *': op = True
                if strlist[iiii] == ' /': op = True
                if strlist[iiii] == ' &&': op = True
                if strlist[iiii] == ' ||': op = True
                if strlist[iiii] == ' ^^': op = True
                if strlist[iiii] == ' ==': op = True
                if strlist[iiii] == ' !=': op = True
                if strlist[iiii] == ' >=': op = True
                if strlist[iiii] == ' <=': op = True
                if strlist[iiii] == ' >': op = True
                if strlist[iiii] == ' <': op = True
                if not iiii > 0:
                    valid = False
                if not iiii < len(strlist):
                    valid = False
                if op:
                    valid = False
                if valid and (strlist[iiii-1] == ' -(' and strlist[iiii+1] == ' -)'):
                    caught = True
                    strlist.pop(iiii-1)
                    strlist.pop(iiii)
                    break
                iiii+=1
                
        i+=1
    print(vars)
    print(strlist)
    return strcode, vars[len(vars)-1], linestoadd

file = open("tokens.txt", "r")
filestr = file.read()





strlist = []
characc = ""
for char in filestr:
    if char != "\n":
        characc += char
    else:
        if characc != "":
            strlist.append(characc)
            characc = ""

print(strlist)

file.close()

file = open("IR.txt", "w")
mode = ""
args = []
varstring = " --"
index = 0
tempstr = ""
tempstr2 = ""
newstr = ""
filestart = 0
asmline = 1
funcscope = 0
functionlines = []
opstring = []
indentation = 0
functionsdefined = []
tempstr3 = ""
tempstr5 = ""
while len(strlist) > index:
    instruction = strlist[index]
    if mode == "call":
        match instruction:
            case " -)":
                mode = ""
                calledfunction = args[0]
                tempstr2 = "#call *" + calledfunction
                asmline+=1
                for i in range(1,len(args)):
                    tempstr2 += " " + args[i] 
                newstr+=tempstr2 + "\n"
                args = []
            case " -b":
                if tempstr != "":
                    args.append(tempstr)
                    tempstr = ""
            case _:
                if instruction != " -(" and instruction != " -)" and instruction != "":
                    tempstr += instruction
    if mode == "params":
        match instruction:
            case " -)":
                mode = ""
            case " -b":
                print(tempstr, "tempstr")
                newstr += tempstr
                tempstr = ""
            case _:
                tempcounter = 0
                if instruction != " int" and instruction != " -)" and instruction != " -(":
                    tempstr += "resv " + instruction + "\n"
    if mode == "function":
        match instruction:
            case " -b":
                functionlines.append(asmline)
                mode = ""
                filestart +=1
                mode = "params"
                functionsdefined.append(tempstr)
                
                tempstr = "func "+ tempstr +"\n"
                funcscope = 1
            case _:
                tempstr = instruction
    if mode == "eq": 
        match instruction:
            case " -b":
                print(opstring)
                tempstr2, var, asmlineplus = equate(opstring, asmline)
                print(tempstr2)
                opstring = []
                newstr += tempstr2 
                newstr += tempstr +" "+ var + "\n"
                
                tempstr4 = tempstr.split()
                if tempstr3 != "":
                    newstr += tempstr3 + tempstr4[1] + "\n"
                tempstr = ""
                asmline+= asmlineplus
                mode = ""
            case _:
                if instruction != "=":
                    opstring.append(instruction)
    if mode == "logic":
        print("no")
        mode = ""
    if mode == "":
        match instruction:
            case " -b":
                newstr += tempstr                
                tempstr = ""
            case " return":
                tempvar = strlist[index+1]
                newstr += "retr " + tempvar + "\n"
                index+=1
            case " if":
                tempstr3 = "if "
                tempstr5 = "ifclose "
                asmline+=1
            case " int":
                tempstr += "ld "
                asmline+=1
            case " -}":
                if tempstr5 == "ifclose ":
                    newstr += "closeif\n"
                    tempstr5 = ""
                indentation -=1
                if funcscope == 1 and indentation == 0:
                    newstr += "funclose\n"
                    funcsope = 0

            case " -{":
                indentation +=1 
            case " =":
                mode = "eq"
            case " call":
                mode = "call" 
            case " function":
                mode = "function" 
            case _:
                cantuse = [" =", " -{", " -}", " -)", " -("]
                if not instruction in cantuse:
                    tempstr += instruction
    index+=1
funcstracc = []
        


            
file.write(newstr)

file.close()
