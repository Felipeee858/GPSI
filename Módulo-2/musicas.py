números_musica= int(input("Indique a quantidade de música:"))
while números_musica <=0:
        print("Valor não é válido")
        números_musica= int(input("Indique a quantidade de música:"))

for i in range(números_musica):
        valor_minutos=int(input("Insira a duração em minutos:"))    
        while valor_minutos <= 0 or valor_minutos>=6000:
                print("Valor não é válido")
                valor_minutos=int(input("Insira a duração em minutos:"))    
# perguntar se deseja inserir mais música.
perguntar=(input("Deseja inserir mais música?"))
if perguntar == ("sim") and ("Sim"):
                numero_musica =float(input("Insira a duração da música:"))
else:    
    perguntar == ("não") and ("Não")
    numero_musica=0

minutos_total= valor_minutos + numero_musica
minutos=minutos_total // 60
segundos= minutos_total % 60
print("A duração total do album é de",minutos,":",segundos)
        
                
        