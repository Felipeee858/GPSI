"""
Programa para testar as credencias (email e password)
Permitir três tentativas
"""


email=input("Introduza o email:")
password=input("Introduza a password: ")
for i in range(3):
    Entrada_Email=input("Introduza o email de entrada: ")
    Entrada_password=input("Introduza a password de entrada: ")
    if Entrada_Email == email and Entrada_password==password:
        print("Entrada concluida")
        break
    elif Entrada_Email != email and Entrada_password != password:
        print("Email e Password erradas")
    elif Entrada_Email != email:
        print("Email Inválido")
    elif Entrada_password != password:
        print("Password Inválida")
if i == 2:
    print("Acabou as tentativas")
