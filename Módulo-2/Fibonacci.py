x1= 0
x2 = 1
n=int(input("Indique um número:"))
print(x1,"\n",x2)
for i in range(n-2):
    soma = x1 + x2
    print(soma)
    x1= x2
    x2=soma
    
