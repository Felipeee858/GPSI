#programa para ler 10 números e indicar qual é o maior
Maior=1
for _ in range(10):
    n=int(input("Introduza o número:"))
    if n>Maior:
        Maior = n 
print("O maior é",Maior)