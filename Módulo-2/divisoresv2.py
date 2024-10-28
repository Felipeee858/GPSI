n=int(input("Insira um número inteiro:"))
divisor=n
while divisor > 0:
    if n % divisor == 0:
        print(divisor)
    divisor = divisor - 1