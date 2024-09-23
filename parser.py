def checkin(xlist, possiblevar):
    for i in range(0,len(possiblevar)):
        if not possiblevar[i] in xlist:
            return possiblevar[i]
    return False


def equate(strlist, asmline):
    print(strlist)
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
            vars.append(newvar)
            strlist[i] = newvar
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
            if not strlist[i] in vars:
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
                
            iiii = 0
            stage = 0
            list_vals_in_func = []
            func_name = -1
            func_range = -1
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
                print(strlist[iiii], "stage: "+ str(stage))
                if stage == 2 and op == False:
                    list_vals_in_func.append(strlist[iiii])
                if op == False and stage == 0:
                    stage = 1 
                    func_range = iiii
                    func_name = iiii
                    print(func_name)
                elif strlist[iiii] == " -(" and stage == 1:
                    stage = 2
                elif strlist[iiii] == " -)" and stage == 2:
                    newarg = checkin(vars, possiblevars)
                    strcode += "#call " + newarg + " *" + vars[func_name]
                    for aeaee in list_vals_in_func:
                        if type(aeaee) == int:
                            strcode += " " + vars[aeaee]
                    stage = 0
                    for list_index in range(func_range+1,iiii+1):
                        strlist.pop(func_range)
                    strlist[func_range] = len(vars)
                    vars.append(newarg)
                    strcode += "\n"
                elif op == True:
                    stage = 0
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
                    tempstr3 = ""
                tempstr = ""
                asmline+= asmlineplus
                mode = ""
            case _:
                if instruction != "=":
                    opstring.append(instruction)
    if mode == "logic":
        print("no")
        mode = ""
    if mode == "writec":
        match instruction:
            case " -b":
                mode = ""
                
                tempstr = "WRC "+ tempstr +"\n"
                newstr += tempstr
                tempstr= ""
            case _:
                tempstr = instruction
    if mode == "readc":
        match instruction:
            case " -b":
                mode = ""
                
                tempstr = "RDC "+ tempstr +"\n"
                newstr += tempstr 
                tempstr= ""
            case _:
                tempstr = instruction

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
                tempstr3 = "bnz "
                tempstr5 = "ifclose "
                asmline+=1
            case " while":
                newstr += "openloop\n"
                tempstr3 = "bnz "
                tempstr5 = "ifloop "
                tempstr = ""
                asmline+=2
            case " int":
                tempstr += "ld "
                asmline+=1
            case " -}":
                if tempstr5 == "ifclose ":
                    newstr += "closeif\n"
                    tempstr5 = ""
                if tempstr5 == "ifloop ":
                    newstr += "closeloop\n"
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
            case " writec":
                mode = "writec" 
            case " readc":
                mode = "readc" 
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
