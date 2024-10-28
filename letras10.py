contar=0
for i in range(10):
    letras=input("Introduza uma letra:")

    for frase in letras:
        if frase in "aeiouAEIOU":
            contar=contar+1
print("A frase indicada tem",contar,"vogais")