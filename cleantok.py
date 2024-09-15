file = open("tokens.txt","r")
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

newstr = []
varsmin = []
varsmax = []
for index, line in enumerate(strlist):
    if line != "":
      newstr += line + "\n"  
    
stracc = ""
for i in range(0,len(newstr)):
    stracc += newstr[i]
file = open("tokens.txt","w")
file.write(stracc)
file.close()
