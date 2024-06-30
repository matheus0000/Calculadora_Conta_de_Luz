def calcular_tarifa_por_kwh(consumo_kwh, valor_total):
    # Verificar se o consumo é maior que zero para evitar divisão por zero
    if consumo_kwh > 0:
        tarifa_por_kwh = valor_total / consumo_kwh
        return tarifa_por_kwh
    else:
        return None  # Retornar None se o consumo for zero ou negativo

# Exemplo de utilização:
consumo = float(input("Digite o consumo de energia em kWh: "))
valor_total = float(input("Valor que você paga na conta de Luz (R$) : "))

tarifa = calcular_tarifa_por_kwh(consumo, valor_total)

if tarifa is not None:
    print(f"A tarifa por kWh é aproximadamente R$ {tarifa:.4f} por quilowatt-hora.")
else:
    print("Erro: O consumo de energia deve ser maior que zero.")
