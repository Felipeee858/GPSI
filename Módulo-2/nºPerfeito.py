#Nº Perfeito
#Soma Divisores = nº
#1+2+3 = 6
#1+2+5 != 10

"""
Algoritmo para dizer os Nºs Perfeitos
"""

n=int(input("Introduza o número:"))
Soma=n
for i in range(1,n):
    if n % i == 0:
        Soma=Soma-i
if Soma==0:
    print("Número Perfeito")
else:
    print("Não é um Número Perfeito")



    """
    numero=int(input("Introduza um nº:"))
    soma=0
    for i in range(1,numero):
    resto = numero % i
        if resto ==0:
        soma = soma + i
    if soma == numero:
        print("Nº é Perfeito")
    else:
        print("Nº não é perfeito. A soma dos seus divisores foi ",soma)

    """