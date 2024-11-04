#programa que verifica a classe que pertence um jogador pela idade
idade=int(input("Introduza a sua idade:"))
if idade <10:
    print("Infantis")
if idade >=10 and idade <14:
    print("Iniciados")
if idade >=14 and idade <18:
    print("junior")
if idade >=18:
    print("seniores")
        