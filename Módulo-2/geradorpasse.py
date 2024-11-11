import random
a_M="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a_m="abcdefghijklmnopqrstuvwxyz"
numero="1234567890"
carater="!?@€.,;:-_"
ppasse=""
for i in range(2):
    Pos=random.randint(0,len(a_M))
    ppasse=ppasse + a_M[Pos]

for i in range(2):
    Pos2=random.randint(0,len(a_m))
    ppasse=ppasse + a_m[Pos2]
for i in range(2):
    Pos3=random.randint(0,len(numero))
    ppasse=ppasse + numero[Pos3]
for i in range(2):
    Pos4=random.randint(0,len(carater))
    ppasse=ppasse + numero[Pos4]

print(ppasse)





