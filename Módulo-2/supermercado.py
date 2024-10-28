#Ler o orçamento e o peso do utilizador
orçamento=float(input("Indique o seu orçamento:"))
peso=float(input("Indique o seu peso:"))
#enquanto tiver orçamento e peso
while orçamento >0 or peso >0:
    #ler o preço e o peso do produto comprado
    preco= float(input("Indique o preço do produto comprado:"))
    #se o peso é zero terminar o ciclo
    if peso == 0:
        break
    peso_produto= float(input("Indique o peso do produto comprado:"))
    #Não posso ultrapassar o orçamento nem o peso
    if orçamento < preco and peso < peso_produto:
        print("Não tem dinheiro ou produto muito pesado")
    else:
        #atualizar o orçamento e o peso
        orçamento = orçamento - preco
        peso = peso - peso_produto
    #mostrar o orçamento e o peso restante 
    print("Ainda tem",orçamento,"€ e ainda pode carregar mais",peso,"Kg")

