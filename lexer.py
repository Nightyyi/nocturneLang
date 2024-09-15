file = open("code.txt", "r")

strf = file.read()
file.close()

charlist = []
characcul = ""
op = False
for i in range(0, len(strf)):
    char = strf[i]  
    add = True
    addend = True
    ## operations
    if char == "+":
        charlist.append(characcul)
        charlist.append(" +")
        characcul = "" 
        add = False
    if char == "-":
        charlist.append(characcul)
        charlist.append(" -")
        characcul = ""
        add = False
    if char == "*":
        charlist.append(characcul)
        charlist.append(" *")
        characcul = ""
        add = False
    if char == "/":
        charlist.append(characcul)
        charlist.append(" /")
        characcul = ""
        add = False
    if char == "!":
        if op == False:
            charlist.append(characcul)
            charlist.append(" !")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "!"
    elif char == "<":
        if op == False:
            charlist.append(characcul)
            charlist.append(" <")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "<"
    elif char == ">":
        if op == False:
            charlist.append(characcul)
            charlist.append(" >")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += ">"
    elif char == "^":
        if op == False:
            charlist.append(characcul)
            charlist.append(" ^")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "^"
    elif char == "|":
        if op == False:
            charlist.append(characcul)
            charlist.append(" |")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "|"
    elif char == "&":
        if op == False:
            charlist.append(characcul)
            charlist.append(" &")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "&"
    elif char == "=":
        if op == False:
            charlist.append(characcul)
            charlist.append(" =")
            characcul = ""
            add = False
            op = True
        else:
            characcul = ""
            charlist[len(charlist)-1] += "="
    else: 
        op = False
    ## single characters
    if char == ";":
        charlist.append(characcul)
        charlist.append(" -b")
        characcul = ""
        add = False
    if char == "(":
        charlist.append(" -(")
        characcul = ""
        add = False
    if char == ")":
        charlist.append(characcul)
        charlist.append(" -)")
        characcul = ""
        add = False
    if char == "{":
        charlist.append(" -{")
        characcul = ""
        add = False
    if char == "}":
        charlist.append(" -}")
        characcul = ""
        add = False
    ##
    ## keyword strings
    ##
    if characcul == "function":
        charlist.append(" "+characcul)
        characcul = ""
        add = False
    if characcul == "if":
        charlist.append(" "+characcul)
        characcul = ""
        add = False
    if characcul == "return":
        charlist.append(" "+characcul)
        characcul = ""
        add = False
    if characcul == "call":
        charlist.append(" "+characcul)
        characcul = ""
        add = False
    if characcul == "int":
        charlist.append(" "+characcul)
        characcul = ""
        add = False
    if char == "\n":
        addend = False
    if char == "\t":
        addend = False
    if char == " ":
        addend = False
    if op:
        addend = False
    if not add:
        addend = False
    if addend:
        characcul += char
    

file = open("tokens.txt", "w")
print(charlist)
indentation = 0
for x in charlist:
    if x == " -indent":
        indentation+=1
    if x == " -dedent":
        indentation-=1
    print("|| " * indentation + x)

    file.write(x + "\n")

file.close()
