valorPagar = float(input("Insira preço pagamento: "))

valorPagar = ((valorPagar/100) * 10) + valorPagar

print("Valor total com gorjeta: ", valorPagar)

valorDado = float(input("Insira valor dado ao caixa: "))

while valorDado < valorPagar:
    valorRestante = valorPagar - valorDado
    print("Ainda faltam:" + str(valorRestante) + "€")
    valorDado = float(input("Insira o restante: ")) + valorDado

valorTroco = valorDado - valorPagar

print("Total compra com gorjeta 10%: " + str(valorPagar) + ", Valor dado ao caixa: " + str(valorDado) + ", Valor troco: " + str(valorTroco))