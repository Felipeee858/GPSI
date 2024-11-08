lado1=int(input("Introduza um nº Positivo: "))
lado2=int(input("Introduza um nº Positivo: "))
lado3=int(input("Introduza um nº Positivo: "))

if lado1>0 and lado2>0 and lado3>0:
    if (lado1+lado2)>lado3:
        triângulo=True
    if (lado2+lado3)>lado1:
        triângulo=True
    if (lado1+lado3)>lado2:
        triângulo=True
    if lado1==lado2 and lado1==lado3 and lado2==lado3:
        print("Equilátero")
    if lado
else:
    print("Erro algum nª introduzido é negativo")

