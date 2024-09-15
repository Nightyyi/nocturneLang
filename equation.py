

strlist = [' -(', 'x', ' *', 'y', ' +', 'x', ' -)', ' /', '5']

def checkin(xlist, possiblevar):
    for i in range(0,len(possiblevar)):
        if not possiblevar[i] in xlist:
            return possiblevar[i]
    return False


def equate(strlist):
    indx = 0
    vars = []
    possiblevars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s']
    strcode = ""
    for i in range(0,len(strlist)):
        if strlist[i].isnumeric():
            strcode += "ld " + str(strlist[i])
            newvar = checkin(vars, possiblevars)
            if newvar == False:
                while (True):
                    print("something went wrong")
            strcode += " " + newvar + "\n"
            strlist[i] = newvar
    for i in range(0,len(strlist)):
        op = False
        if strlist[i] == '+': op = True
        if strlist[i] == '-': op = True
        if strlist[i] == '*': op = True
        if strlist[i] == '/': op = True
        if strlist[i] == '(': op = True
        if strlist[i] == ')': op = True
        if op == False:
            vars.append(strlist[i])
            strlist[i] = indx
            indx+=1
    parcounter = 0
    while len(strlist) != 1:
        score = 0
        i = 0
        for ii in range(0,len(strlist)):
            char = strlist[ii]
            if char == '(':
                parcounter+=1
            if char == ')':
                parcounter-=1
            if char == '+':
                newscore = (parcounter*3)+1 
                if newscore > score:
                    i = ii
                    score = newscore
            if char == '-':
                newscore = (parcounter*3)+1 
                if newscore > score:
                    i = ii
                    score = newscore
            if char == '*':
                newscore = (parcounter*3)+2
                if newscore > score:
                    i = ii
                    score = newscore
            if char == '/':
                newscore = (parcounter*3)+2 
                if newscore > score:
                    i = ii
                    score = newscore

        print(i, strlist) 
        if strlist[i] == '+': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "add " + vars[arg1] + " " + vars[arg2] + " -> " + newarg + "\n"
            op = True
        if strlist[i] == '-': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "sub " + vars[arg1] + " " + vars[arg2] + " -> " + newarg + "\n"
            op = True
        if strlist[i] == '*': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "mul " + vars[arg1] + " " + vars[arg2] + " -> " + newarg + "\n"
            op = True
        if strlist[i] == '/': 
            arg1 = strlist[i-1]
            arg2 = strlist[i+1]
            newarg = checkin(vars, possiblevars)
            strlist[i] = len(vars)
            vars.append(newarg)
            strlist.pop(i-1)
            strlist.pop(i)
            i-=1
            strcode += "div " + vars[arg1] + " " + vars[arg2] + " -> " + newarg + "\n"
            op = True
        
        caught = True
        while caught and (len(strlist) > 1):
            caught = False
            iiii = 0
            while iiii < len(strlist):
                op = False 
                valid = True
                if strlist[iiii] == '+': op = True
                if strlist[iiii] == '-': op = True
                if strlist[iiii] == '*': op = True
                if strlist[iiii] == '/': op = True
                if not iiii > 0:
                    valid = False
                if not iiii < len(strlist):
                    valid = False
                if op:
                    valid = False
                if valid and (strlist[iiii-1] == '(' and strlist[iiii+1] == ')'):
                    caught = True
                    strlist.pop(iiii-1)
                    strlist.pop(iiii)
                    break
                iiii+=1
                
        i+=1

    return strcode

neweq = equate(strlist)
print(neweq)
