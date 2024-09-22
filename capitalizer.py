file = open("built", "r")
fcomp = file.read()
file.close()
acc = ""
lines = []
for ch in fcomp:
    if ch == '\n':
        lines.append(acc)
        acc = ""
    else: 
        acc+=ch
print(lines)
    
new_ = ""

for line in lines:
    line_s = line.split()
    new_ += line_s[0].upper() + " "
    line_s.pop(0)
    for i in line_s:

        new_ += i + " "
    new_ += "\n"

file = open("built", "w")
file.write(new_)
file.close() 

