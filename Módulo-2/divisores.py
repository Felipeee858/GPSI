"""
Ler um número inteiro positivo do utilizador e mostrar todos os divisores desse número
P.Ex.:
->6
6
3
2
1
->10
10
5
2
1
"""
n=int(input("Insira um número inteiro:"))
for divisor in range(n,0,-1):
    if n % divisor == 0:
        print(divisor)
