"""
Um programa que lê números do utilizador e indique se são positivos ou negativos e
o programa termina quando em inserio o 0
"""
n=1
while n!=0:
    n=int(input("Introduza um número:"))
    if n>0:
        print("Positivo")
    elif n<0:
        print("Negativo")

