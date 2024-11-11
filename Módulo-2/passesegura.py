
alfabetoM="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabetom="abcdefghijklmnopqrstuvwxyz"
numero="1234567890"
carater="!?@€.,;:-_"
temalfabetoM=False
temalfabetom=False
temnumero=False
temcarater=False
palavra=input("\n1.letras\n2.Maiúscula e minuscula\n3.Tem de ter nºs\n4.Pelo menos 8 carateres\n5.Tem de ter um carater especial: ! ? @€.,;:-_ \n  Introduza a palavra deve conter:")
#testar maiusculas
for letra in alfabetoM:
    if letra in palavra:
        alfabetoM = True
        break
if alfabetoM==True:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")
for letra in alfabetom:
    if letra in palavra:
        alfabetom = True
        break
if alfabetom==True:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")
    for letra in numero:
        if letra in palavra:
            numero = True
            break   
if numero==True:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")
for letra in carater:
    if letra in palavra:
        carater = True
        break
if carater==True:
    print("Palavra passe segura")
else:
    print("Palavra passe não é segura")
