#ferramenta de conversão dolár x real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("conversor dolar x real")
preco = float(input("digite o preço do produto em dolar:"))
resultado = converter(preco)
print(f"o valor em reais é:{resultado:.2f}")
   