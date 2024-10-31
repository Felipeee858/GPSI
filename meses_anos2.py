dia=int(input("Introduza os dias:"))
mes_atual=int(input("Introduza o mes:"))
ano=int(input("Introduza o ano:"))
soma=0
for mes in range(mes_atual,13):
    dias_mes=31

    if mes == 4 or mes==5 or mes== 9 or mes ==11:
        dias_mes=30
    elif mes == 2:
        if (ano % 4 == 0 ans ano % 100 !=0) or ano % 400=0:
            dias_mes = 30
        else:
            dias_mes = 28
    faltam = dias_mes - dia
    dia=0
    soma = soma +faltam
print("Faltam ",soma,"dias para o fim do ano")
