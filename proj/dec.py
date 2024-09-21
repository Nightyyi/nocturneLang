file = open("txtfile.txt","r")
filestr = file.read()
file.close()

strlist = []
characc = ""
for char in filestr:
    if char != "n" and char != "\0":
        if char == '1' or char == '0':
            characc += char
    else:
        strlist.append(characc)
        characc = ""

new_ = ""
linep = 0
for index, line in enumerate(strlist):
    new_ += "ld r59" + line + "\n"
    new_ += "chw r59 " + str(linep) + "\n"
    linep+= len(line)-1
    
file = open("new.txt","w")
file.write(new_)
file.close()
