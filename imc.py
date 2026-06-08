#etapa 1 - calculo do imc
def calc_imc(imc):
    imc = peso /(altura*altura)
    return imc 

    #etapa 2 - classificado do imc
    def classificar_imc(resultados):
        if resultado >= 25:
            return "ACIMA  DO PESO"
        else:
            return "PESO NORMAL"´
#etapa 3 - mensagem de retorno
def mensagem(status):
    if status == "ACIMA DO PESO"
        return "🆘atenção! procure um médico"
    else:
        return "👍seu peso está normal!continue assim"
    
#etapa 4 - integração do codigo
valor_peso = float(input("digite o seu peso"))
valor_altura = float(input("digite sua altura"))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print("="*50)
print("RESULTADO DO SEU IMC")
print(f\n seu IMC é:(valor_imc))
print(f"\n {saida}")
print





