
file = open("IR.txt", "r")

strf = file.read()
file.close()

charlist = []
funclist = []
funcscope = []

characcul = ""
op = False
newstr = ""
mainstr = ""
func_counter = 0
capture = False 
line = []
close_func = False
for ch in strf:
    
    if ch != ' ' and ch != '\n':
        characcul += ch
    if ch == ' ':
        line.append(characcul)
        characcul = ""
    if ch == '\n':
        line.append(characcul)
        characcul = ""
        if line[0] == "funclose":
            funcscope.append(newstr)
            newstr = ""
            capture = 0
            close_func = True
            line = []
        if close_func == False:
            if line[0] == "func":
                funclist.append(line[1])
                capture = 1
                line = []
        if capture == 1:
            for i in line:
                newstr += i + " " 
            if len(line) > 0:
                newstr += "\n"
        elif capture == 0:
            for i in line:
                mainstr += i + " "
            if len(line) > 0:
                mainstr += "\n"
        close_func = False
        line = []


print(funcscope)
print(funclist)
print(mainstr+"\n")

file = open("funcs\\"+"main.txt", "w")
file.write(mainstr)
file.close()

for index,i in enumerate(funcscope):
    print(i)
    file = open("funcs\\"+ funclist[index] +".txt", "w")
    file.write(i)
    file.close()


file = open("funclist.txt", "w")
file.write("main.txt\n")
for i in funclist:
    file.write(i+".txt\n")
file.close()


