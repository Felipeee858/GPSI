"""
O sistema de aquecimento da escola verifica as temperaturas a cada hora de funcionamento. 
A direção precisa de saber qual a amplitude térmica para o período de aulas (das 9 às 17) para 
perceber que temperatura deve ajustar para as salas de aula. Como os Navarros gostam de 
programar de forma confortável vamos ajudar a direção da escola. Para isso deves 
desenvolver um programa que depois de lidas as temperaturas hora a hora possa indicar a 
temperatura mínima e máxima e correspondente amplitude térmica.

"""
tempmax=0
tempmin=1000
amp_temperatura=0
for i in range(9,18):
    print(i,"horas")
    temperatura=int(input("Introduza a temperatura:"))
    amp_temperatura=amp_temperatura+temperatura
    if tempmax<temperatura:
        tempmax=temperatura
    if tempmin>temperatura:
        tempmin=temperatura
print(tempmin,"<-- temperatura mínima")
print(tempmax,"<-- temperatura máxima")
print(amp_temperatura/17,"<-- amplitude térmica")
