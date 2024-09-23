class VarUse:
    def __init__(self, name):
        self.name = name
        self.definer = []
        self.mutator = []
        self.users   = []
    
    def print(self):
        print( "|"+ self.name+"|" )
        strlist = ""
        strlist+="-------def-------\n"
        for definer in self.definer:
            strlist+= definer + ", "
        strlist+="\n-------mut-------\n"
        for mutator in self.mutator:
            strlist+= mutator + ", "
        strlist+="\n-------use-------\n"
        for users in self.users:
            strlist+= users + ", "
        strlist+="\n-----------------\n"
        print(strlist)

def check_if_in(list_of_vars, name):
    for x in list_of_vars:
        if x.name == name:
            return True
    return False

def check_index(list_of_vars, name):
    for index,x in enumerate(list_of_vars):
        if x.name == name:
            return index
    return False
file = open("IR.txt", "r")

strf = file.read()
file.close()

lines = []
acc = ""
for ch in strf:
    if ch == '\n':
        lines.append(acc)
        acc = ""
    else: 
        acc+=ch

var_list = []
for line in lines:
    line_s = line.split()
    instruction = line_s[0]
    variables = line_s[1:]
    if instruction == "ld":
        if not check_if_in(var_list, variables[0]):
            var_list.append(VarUse(variables[0]))
        if check_if_in(var_list, variables[1]):
            print(line)
            index = check_index(var_list, variables[0])
            var_list[index].definer.append(variables[1])
            index = check_index(var_list, variables[1])
            var_list[index].users.append(variables[0])

    inst_list = ["add","sub","div","mul"]
    if instruction in inst_list:
        if not check_if_in(var_list, variables[2]):
            var_list.append(VarUse(variables[2]))
            index = check_index(var_list, variables[2])
            var_list[index].definer.append(variables[0])
            index = check_index(var_list, variables[2])
            var_list[index].definer.append(variables[1])
            index = check_index(var_list, variables[0])
            var_list[index].users.append(variables[2])
            index = check_index(var_list, variables[1])
            var_list[index].users.append(variables[2])
        else:
            index = check_index(var_list, variables[2])
            var_list[index].mutator.append(variables[0])


for item in var_list:
    item.print()
