mesas = 10
mesas = mesas - 1
#ocupar os lugares= 10
lugares = mesas * 5

for mesas_ocupadas in range(mesas):
    nr_clientes = int(input("Quantas pessoas para entrar:"))
if nr_clientes>lugares:
    print("Não tem lugares para tanto clientes")
    breakpoint 
#ocupar 1 mesa
lugares = lugares - nr_clientes
print("Lugares disponíveis: ",lugares)
print("Mesas ocupadas:",mesas_ocupadas+1)
        