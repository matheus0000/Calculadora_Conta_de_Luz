def calculadora_conta_de_luz(consumo_kwh, tarifa_por_kwh):
    # Calcula o valor da conta de luz
    valor_conta = consumo_kwh * tarifa_por_kwh
    return valor_conta

# Exemplo de uso da função
consumo = float(input("Digite o consumo de energia em kWh: "))
tarifa = float(input("Digite a tarifa por kWh: "))

total_conta = calculadora_conta_de_luz(consumo, tarifa)
print(f"O valor da conta de luz é R$ {total_conta:.2f}")
