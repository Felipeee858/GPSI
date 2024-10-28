#ciclo para percorrer a frase letra a letra mas por ordem invertida
frase=input("Introduza uma frase:")
for posiçao in range(len(frase)-1,-1,-1):
    print(frase[posiçao])
    