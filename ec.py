#FUNCIONES DEL PROGRAMA
def isnum(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False
"""
def detx(ec):
    numx =""
    nole = []
    for x in range(len(ec)):
        if ec[x] == 'x':
            nole.append(x)
            for y in range(x-1,-1,-1):
                #print(ec[y])
                #if ec[y] != '-' and ec[y] != '+':
                if isnum(ec[y]) == True:
                    numx = ec[y] + numx
                    nole.append(y)
                else:
                    if ec[y] == " ":
                        print("Los espacios dan errores, vuelve a escribir la ecuación")
                    elif ec[y] =="-":
                        numx = "-" + numx
                        nole.append(y)
                        break
                    elif ec[y] =="+":
                        nole.append(y)
                        break
    return numx, nole

"""

def cnum(ec, nole):
    nole.sort(reverse=True)
    lec = list(ec)
    for x in nole:
       lec.pop(x)
    newc = ""
    for y in lec:
        newc = newc + y
    return newc
def negsum(ec):
    pneg = []
    neg = []
    sum = []
    if ec[0] == "-":
        neg.append("")
        for y in range(1,(len(ec))):
            #if ec[y] != "-" and ec[y] != "+":
            if isnum(ec[y]) == True:    
                neg[0] = neg[0] + ec[y]
            else:
                if ec[y] == ".":
                    neg[0] = neg[0] + ec[y]
                else:
                    break
        pneg.append(ec[0]) 
    else:
        sum.append("")
        for y in range(0,(len(ec))):
            #if ec[y] != "-" and ec[y] != "+":
            if isnum(ec[y]) == True: 
                sum[0] = sum[0] + ec[y]
            else:
                if ec[y] == ".":
                    sum[0] = sum[0] + ec[y]
                else:
                    break
    for x in range(1,len(ec)):
        if ec[x] == "-":
            neg.append("")
            if len(neg) == 1:
                long = 0
            else:
                long = len(neg)-1
            for y in range((x+1),(len(ec))):
                #if ec[y] != "-" and ec[y] != "+":
                if isnum(ec[y]) == True: 
                    neg[long] = neg[long] + ec[y]
                else:
                    if ec[y] == ".":
                        neg[long] = neg[long] + ec[y]
                    else:
                        break
            pneg.append(ec[x]) 
        elif ec[x] == "+":
            sum.append("")
            if len(sum) == 1:
                long = 0
            else:
                long = len(sum)-1
            for y in range((x+1),(len(ec))):
                #if ec[y] != "-" and ec[y] != "+":
                if isnum(ec[y]) == True: 
                    sum[long] = sum[long] + ec[y]
                else:
                    if ec[y] == ".":
                        sum[long] = sum[long] + ec[y]
                    else:
                        break
        elif ec[x] == "(":
            sum.append("")
            if len(sum) == 1:
                long = 0
            else:
                long = len(sum)-1
            for y in range((x+1),(len(ec))):
                #if ec[y] != "-" and ec[y] != "+":
                if isnum(ec[y]) == True: 
                    sum[long] = sum[long] + ec[y]
                else:
                    if ec[y] == ".":
                        sum[long] = sum[long] + ec[y]
                    else:
                        break
    return neg, sum, pneg
def paren(ec):
    #detectar parentesis, en caso contrario deja la ecuacion igual
    muls = []
    neg = [0]
    sum = [0]
    for x in range(len(ec)):
        if ec[x] == "(":
            inside = ""
            for y in range((x+1), len(ec)):
                if ec[y] == ")":
                    break
                else:
                    inside = inside + ec[y]
            # (-3x + 2)
            #nx,nole = detx(inside)
            newinside = cnum(inside, nole)
            neg, sum, pneg = negsum(newinside)
            mul = ""
            menos =int(-1)
            for z in range((x-1),-1,-1):
                if isnum(ec[z]) == True: 
                    mul = ec[z] + mul
                if isnum(ec[z]) == False:
                    if mul != "":
                        break
                    else: 
                        if ec[z] == "+":
                            return neg, sum
                        if ec[z] == "-":
                            neg, sum = sum, neg
                            return neg, sum
            sum = [float(i) for i in sum]
            print(sum)
            neg = [float(i) for i in neg]
            print(neg)
            tsum = sum
            tneg = neg
            mul = float(mul)
            muls.append(mul)
            for i in range(len(sum)):
                tsum[i] = float(sum[i]) * mul
            for i in range(len(neg)):
                tneg[i] = float(neg[i]) * mul
            try: 
                neg[0] = neg[0] + 0
            except:
                neg.append(0)
            try: 
                sum[0] = sum[0] + 0
            except:
                sum.append(0)
    return tneg, tsum, muls, neg, sum
    
def mul(ec):
    rmul = []
    muls = []
    for x in range(len(ec)):
        if ec[x] == "*":
            mul1 = ""
            for y in range((x-1),-1,-1):
                if isnum(ec[y]) == True:
                    mul1 = ec[y] + mul1
                if isnum(ec[y]) == False:
                    if ec[y] == "-":
                        mul1 = ec[y] + mul1
                    elif ec[y] == ".":
                        mul2 = ec[y] + mul2
                    else:
                        break
            muls.append(mul1)
            print(mul1)
            mul2 = ""
            sign = 0
            for y in range((x+1),len(ec)):
                if isnum(ec[y]) == True:
                    mul2 = ec[y] + mul2
                if isnum(ec[y]) == False:
                    if ec[y] == "-" and sign==0:
                        mul2 = ec[y] + mul2
                    if ec[y] == ".":
                        mul2 = ec[y] + mul2
                    else: 
                        break
            muls.append(mul2)
            print(mul2)
            rmul.append((float(mul1)*float(mul2)))
    return rmul, muls

#INCIO DEL PROGRAMA
ec = input("Introduce la ecuacion")
#numx, nole = detx(ec)
#print("La parte de la x es: ",numx)
#print(nole)
nole=[]
num = cnum(ec,nole)
neg, sum, pneg = negsum(num)
inneg, insum, pmulsm, innegn, insumn = paren(ec)
#print(inneg)
if inneg[0] != 0 or insum[0] != 0:
    pposi = float(0)
    pnega = float(0)
    for x in inneg:
        pposi += x
    for y in insum:
        pnega += y
    parsol = float(pposi + pnega)
else: 
    parsol = 0
rmul,muls = mul(ec)
#print(muls, "muls")
sum = [float(i) for i in sum]
neg = [float(i) for i in neg]
muls = [float(i) for i in muls]
for x in muls:
    for y in range(len(sum)):
        if x == sum[y]:
            sum.pop(y)
            break
    for y in range(len(neg)):
        if x == neg[y]:
            neg.pop(y)
            break
for x in pmulsm:
    for y in range(len(sum)):
        if x == sum[y]:
            sum.pop(y)
            break
    for y in range(len(neg)):
        if x == neg[y]:
            neg.pop(y)
            break
#print(inneg)
#print(insum)
#print(sum)
print(insum, "ins")
print(innegn, "inn")
print(sum, "sum")
for x in insumn:
    for y in range(len(sum)):
        if x == sum[y]:
            sum.pop(y)
            break
for x in innegn:
    for y in range(len(neg)):
        if x == neg[y]:
            neg.pop(y)
            break
print(sum, "sum")
"""
print("Los numeros negativos fuera de los paréntesis son: ")
for x in neg:
    print(x, end="  ")
print("")
print("Los numeros positivos son: ")
for x in sum:
    print(x, end="  ")
print("")

"""

#solucion

sol = float() 
for x in sum:
    print(x, "sum")
    sol += x
for x in neg:
    print(x, "neg")
    sol += x
for x in rmul:
    print(x, "rmul")
    sol +=x
sol += parsol

print("La solución es ", sol)