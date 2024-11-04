"""
Faça um algoritmo para calcular um valor A elevado a um expoente B (
B A
). Os valores A e 
B deverão ser lidos. Não usar a operação aritmética A ^ B
"""
resultado=1
A=int(input("Introduza o número:"))
B=int(input("Introduza o expoente:"))
for i in range (1,B+1):
    resultado=resultado*A
print(resultado)