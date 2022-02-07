def Mcm():
    nmultiplos = [7,5,3,2]
    #multiplos = [[],[]]
    tdosmultiplos = int(1)
    #repetidos = [{},{}]
    numeros = []
    metidos = []
    flag = 1

    print("Numeros del MCM: ")
    entrada = str(input())

    conte = 0
    contm = 0
    numeros.append(str())
    templ = []
    first = 1
    for x in entrada:
        if x == ",":
            templ.append(len(range(0,contm)))
            contm += 1
        elif x != ",":
            contm += 1
    templ.append(len(range(conte,contm)))
    #print (templ)
    for y in templ:
        if first == 1:
            for x in range(0,y):
                numeros[conte] = int((f"{numeros[conte]}{entrada[x]}"))
            conte = 1
            anty = -1
            first = 0
        else:
            anty += 1 
            numeros.append(str())
            for x in range(templ[anty] + 1,y):
                numeros[conte] = int((f"{numeros[conte]}{entrada[x]}"))
            conte += 1
            


    #print(numeros)

    reps = int(len(numeros))


    multiplos = [[]for x in range(reps)]
    repetidos = [{}for x in range(reps)]

    for y in range(reps):
        temp = int(numeros[y])
        for x in nmultiplos:
            while temp % x == 0: 
                temp = temp/x
                multiplos[y].append(x)
                flag +=1
        if flag == 1:
            multiplos[y].append(int(numeros[y]))
        flag = 1


    #print(multiplos[2])
    #print(multiplos[0])

    for z in range(reps):
        for x in range(len(multiplos[z])):
            repetidos[z].update({f"{multiplos[z][x]}": int(1)})
            for y in range(len(multiplos[z])): 
                if (multiplos[z][x] == multiplos[z][y]) and x!=y:
                    repetidos[z].update({f"{multiplos[z][x]}": repetidos[z][f"{multiplos[z][x]}"] + 1})

    # print(repetidos[0])
    # print(repetidos[1])
    # print(repetidos[2])
    # falta cambiar esto

    multiplosnum =[]
    for z in range(reps):
        for x in range(len(multiplos[z])):
            multiplosnum.append(multiplos[z][x])

    multiplosnum = list(set(multiplosnum))
    #print(multiplosnum)
    masalto= []

    for x in multiplosnum:
        for z in range(reps):
            if f'{x}' in repetidos[z]:
                masalto.append(repetidos[z][f'{x}'])
                #print(x,":",repetidos[z][f'{x}'])
        #print(masalto)
        masalto.sort(reverse=True)
        tdosmultiplos *= x ** masalto[0]
        #print(tdosmultiplos)
        masalto= []
        
    print("MCM es: ",tdosmultiplos)

def Sum():
    print("Numeros de la Suma: ")
    entrada = str(input())
    numeros = []
    conte = 0
    contm = 0
    numeros.append(str())
    templ = []
    first = 1
    for x in entrada:
        if x == ",":
            templ.append(len(range(0,contm)))
            contm += 1
        elif x != ",":
            contm += 1
    templ.append(len(range(conte,contm)))
    #print (templ)
    for y in templ:
        if first == 1:
            for x in range(0,y):
                numeros[conte] = int((f"{numeros[conte]}{entrada[x]}"))
            conte = 1
            anty = -1
            first = 0
        else:
            anty += 1 
            numeros.append(str())
            for x in range(templ[anty] + 1,y):
                numeros[conte] = int((f"{numeros[conte]}{entrada[x]}"))
            conte += 1
    
    tot = 0
    for x in numeros:
        tot += x
    
    print ("La suma de todos los numeros es", tot)
#inicio del programa

print("Escribe lo que deseas hacer")
print("Suma = SUM")
print("Minimo Comun Multiplo = MCM")

x = input()

if x[0]== 'M' and x[1] == 'C' and x[2]=='M':
    Mcm()
if x[0]== 'S' and x[1] == 'U' and x[2]=='M':
    Sum()