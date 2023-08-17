dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))
ganho_horas = (dias_trabalhados * 8) * 25

print(f"Com {dias_trabalhados} dias trabalhados, você ganhará: ")
print("R$ %.2f" % ganho_horas)
