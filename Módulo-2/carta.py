pontos = 12
Infração= 0
Infração_leve=0
Infração_grave=0
Infração_Mgrave=0
while Infração !="4":
    #mostrar pontos
    print("Pontos:",pontos)
    if pontos==0:
        print("Perdeu a sua carta")

    #mostrar as opções
    print("1.MuitoGrave\n2.Grave\n3.Leve\n4.Terminar")
    #Ler opção
    Infração=input(":")
    #retirar os pontos
    if Infração=="1":
        pontos = pontos - 6
        Infração_Mgrave= Infração_Mgrave + 1
    if Infração=="2":
        pontos = pontos - 4
        Infração_grave= Infração_grave + 1
    if Infração == "3":
        if Infração_leve>0:
            pontos = pontos -1
        Infração_leve = Infração_leve + 1
    #se  tem uma infração muito grave e uma grave ou 2 graves perde os pontos todos
    if (Infração_Mgrave==1 and Infração_grave==1) or (Infração_grave==2):
        pontos=0
    if pontos <0:
        pontos=0