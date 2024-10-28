contar = 0
while contar < 5:
    n=int(input("Introduza um número > 10 e < 100"))
    if n > 10 and n < 100:
        contar = contar + 1
    else:
        print("Valor inválido") 
print(contar)
        

