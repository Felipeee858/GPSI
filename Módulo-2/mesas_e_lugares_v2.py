mesas = 10
lugares = mesas * 5

while mesas>0:
    nr_clientes = int(input("Quantas pessoas para entrar:"))
if nr_clientes>lugares:
    print("Não tem lugares para tanto clientes")
    breakpoint 
#ocupar 1 mesa
mesas = mesas - 1
#ocupar os lugares
lugares = lugares - nr_clientes
print("Mesas ocupadas:",10 - mesas)
print("Lugares disponíveis: ",lugares)
        