"""
Um programa que solicita ao usuario um n inteiro positivo e imprime a sequência de Collatz
até chegar em 1
"""


nº=int(input("Introduza um nº inteiro positivo: "))
nº1=nº
contarp=0
while nº != 1:
    if nº % 2 == 0:
        nº= nº // 2
        print(nº)
        contarp=contarp + 1
        continue
        
    else:
        nº= nº *3 + 1
        print(nº)
        contarp=contarp + 1
        continue
print("O número de passos: ",contarp)
