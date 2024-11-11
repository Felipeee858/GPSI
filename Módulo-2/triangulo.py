a=int(input("Introduza um nº Positivo: "))
b=int(input("Introduza um nº Positivo: "))
c=int(input("Introduza um nº Positivo: "))

if a<= 0 or b<= 0 or c <= 0 or c<=0 or a+b < c or a+c<b or b+c<a:

else:
#CLASSIFICAR O TRIANGULO
if a ==b and b==c:
    print("Equilátero")
#se dois iguais
elif a==b or a == c or b==c:
    print("Isosceles")
else:
        print("Escaleno")
