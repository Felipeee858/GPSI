numero=int(input("Introduza um nº:"))
for k in range(1,numero):
    soma=0
    for i in range(1,k):
        resto = k % i
        if resto ==0:
            soma = soma + i
    if soma == k:
            print("Nº",k,"é Perfeito")
    else:
        print("Nº",k,"não é perfeito. A soma dos seus divisores foi ",soma)
