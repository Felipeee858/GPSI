dias=int(input("Introduza os dias:"))
meses_atual=int(input("Introduza o mes:"))
ano=int(input("Introduza o ano:"))

for meses in range(meses_atual,13):
    if meses == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            total_meses= 29 - dias
            print("Falta",total_meses)
        else: 
            total_meses28= 28 - dias
            print("Falta",total_meses28)
    if meses == 1 or meses == 3 or meses == 5 or meses ==7 or meses ==8 or meses ==10 or meses ==12:
        total_meses31= 31 - dias
        print("Falta",total_meses31)
    if  meses == 4 or meses == 6 or meses == 9 or meses ==11:
        total_meses30= 30 - dias
        print("Falta",total_meses30)

