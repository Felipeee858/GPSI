soma=0
x=float(input("Indique o Número:"))
x= x + 0.5
for i in range (10):
    if i<9:
        print(x,end=",")
    else:
        print(x,end="")
    x= x + 0.5
    soma = soma + x

print(" =",soma)


