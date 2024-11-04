"""
Os Navarros decidiram fazer um Kartódromo para se divertirem quando não têm testes para 
fazer. Cada corrida é composta por 5 voltas. Para saber o tempo que cada piloto demora a 
fazer a prova é necessário registar os tempos de cada volta. A tua missão é criares o programa 
que permita ler os tempos à passagem na meta e no fim de 5 voltas mostre no ecrã da Box o 
tempo total despendido.#dependido (soma de todos)
"""

pilotos=int(input("Indique os pilotos:"))

for i in range(pilotos):
    Volta1=int(input("Introduza o Valor do tempo:"))
    Volta2=int(input("Introduza o Valor do tempo:"))
    Volta3=int(input("Introduza o Valor do tempo:"))
    Volta4=int(input("Introduza o Valor do tempo:"))
    Volta5=int(input("Introduza o Valor do tempo:"))
    Soma=Volta1+Volta2+Volta3+Volta4+Volta5
    print(Soma)
   

