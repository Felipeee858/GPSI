"""
Ler dois números e dizer se são Iguais ou diferentes se for diferentes fazer a diferença e se o valor for negativo
tem que o mostrar positivo
"""


n1 = int(input())
n2 = int(input())

if n1==n2:
    print("Iguais")
else:
    print("Diferentes")
    diferença=n1-n2
    if diferença<0:
        diferença=diferença*(-1)
    print(diferença)