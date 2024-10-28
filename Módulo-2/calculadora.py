#Pedir ao utilizador a conta que ele quer fazer


escolha ="s"
while escolha == "s" or escolha == "sim":
    n1=float(input("Introduza um número:"))
    n2=float(input("Introduza outro número:"))
    Subtração=n1 - n2
    Adição= n1 + n2
    Multiplicação= n1*n2
    Divisão= n1/n2
    perguntar=input("Deseja fazer qual operação?")
    if perguntar == "Multiplicação" or perguntar == "multiplicação":
        print(Multiplicação)

    elif perguntar == "Subtração" or perguntar == "subtração":
        print(Subtração)
        
    elif perguntar == "Divisão" or perguntar == "divisão":
        print(Divisão)
        
    elif perguntar == "Adição" or perguntar == "Adição":
        print(Adição)
    elif perguntar== "Somatório" or perguntar =="somatório":
        soma=0
        n3=int(n1)
        n4=int(n2)
        for i in range(n3,n4):
            soma=soma+i
            print(soma)
    
    escolha=input("Pretende continuar a fazer contas?")
    escolha=escolha.strip().lower()




