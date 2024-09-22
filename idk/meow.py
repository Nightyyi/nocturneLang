import random

listn = [5,0,2,4,1,3,6]
listo = [5,0,2,4,1,3,6]
target= [0,1,2,3,4,5,6]
print(listn)




lines = 0
for uruwrt in range(0,1000):
    listn = [x for x in range(0,64)] 
    listo = [x for x in range(0,64)] 
    target = [x for x in range(0,64)] 

    i_set = [] 
    n = 32
    while (n >= 0):
        i = random.randint(0,63)
        ii = random.randint(0,63)
        if not (i in i_set):
            i_set.append(i)
            i_set.append(ii)
            x = listn[ii]
            y = listn[i]
            if x != y:
                listn[ii] = y
                listn[i]  = x
        else:
            n+=1
        n-=1

    do = True
    strnew = ""
    while do:
        do = False
        for zz in range(0,len(listn)):
            i = target[listo.index(zz)]
            x = listn[listn[i]]
            y = listn[i]
            if x != y:
                listn[listn[i]] = y
                listn[i]        = x
                strnew += "swp r" + str(x) + " r" + str(y) + "\n"
                do = True
                lines+=1
    print(strnew)
    print(lines)


