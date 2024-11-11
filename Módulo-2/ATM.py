"""
ATM
1 Ver saldo
2 Depositar Dinheiro
3 levantar Dinheiro
4 Terminar
"""
Saldo=0
print("1 Ver Saldo")
print("2 Depositar Dinheiro")
print("3 Levantar Dinheiro")
print("4 Terminar")
opção=0
while opção <=3 and Saldo <0:
    opção=int(input("Introduza o nº: "))
    if opção == 1 and Saldo >= 0:
        print(Saldo)
        
    if opção == 2 :
        deposito=float(input("Insira a quantidade de Dinheiro que deseja depositar:"))
        Saldo = Saldo + deposito
        #testar nº de casas decimais
        d= deposito - round(deposito,2)
        if d !=0:
            print("O valor não é válido, só pode ter 2 casas decimais")
            continue

        if deposito < 0.01 or deposito >10000:
            print("Excedeu ou ultrapassou o limite de depositar dinheiro")
            continue
        
    if opção == 3 and Saldo>=0:
        levantar=float(input("Introduza a quantidade de Dinheiro para levantar: "))
        Saldo=Saldo-levantar
        if Saldo < 0:
            print("Erro")
        
            if levantar< 10 or levantar > 400:
                print("Excedeu ou ultrapassou o limite de levantar dinheiro")
print("Terminou")
        

