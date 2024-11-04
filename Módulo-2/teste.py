dias=int(input("Introduza os dias:"))
meses=int(input("Introduza o mes:"))
ano=int(input("Introduza o ano:"))
anos_meses= 12 - meses
if meses == 4 or meses == 6 or meses == 9 or meses ==11:
    meses_dias= meses * 30
    dias1= 365 - meses_dias + 7
    print("Falta",dias1,"ou",anos_meses)
if meses == 1 or meses == 3 or meses == 5 or meses ==7 or meses ==8 or meses ==10 or meses ==12:
    meses_dias = meses * 31 
    dias2= 365 - meses_dias - 4
    print("Falta",dias2,"ou",anos_meses)


