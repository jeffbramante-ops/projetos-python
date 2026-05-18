#--simulador de investimento - poupança--
deposito =float(input("digite o valor do aporte"))
taxa =float(input("qual a taxa da poupança em % ?"))
meses = int(input("quantos meses vai investir?"))
conversao = taxa/100
total = 0
for mes in rangel(1,meses +1):
    total = total + deposito
    total = total + (total * taxa)
print(f"ao final do periodo,voce tera:r${total:.2f}")