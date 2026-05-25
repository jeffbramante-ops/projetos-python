#multiplas funções--exercicio controle de qualidade--
def cabecalho():
    print("\n" + "=" *30)
    print("sistema de qualidade")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
       return "aprovada"
    else:
       return "reprovada"
cabecalho()
peso_item = float(input("digite o peso do item em gramas:"))
status = verificar_status(peso_item)
print(f"resultado da inspeção:{status}")
print("=" * 30)

    