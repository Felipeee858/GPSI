"""
Uma transportadora área possui um avião que no porão consegue carregar 1000 Kg de carga. 
Em cada viagem a empresa cobra uma taxa de 20 € por cada mala que transporta. Como o 
peso da carga não pode exceder os 1000 kg é necessário saber no processo de Check In o 
peso de cada mala. Neste exercício deves preparar um programa que leia o peso das malas de 
forma sucessiva e quando o limite da carga for atingido deve indicar que se atingiu o limite 
permitido mostrando de seguida o valor apurado em taxas.
"""
peso=0

while peso <=1000:
    peso1=int(input("Introduza o peso da mala:"))
    peso=peso+peso1
print("Atingiu o limite")
#Não acabado

