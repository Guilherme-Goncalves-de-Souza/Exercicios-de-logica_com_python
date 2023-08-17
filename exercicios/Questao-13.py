salario = int(input("Digite o salário: "))
aumento = int(input("Digite o % de aumento: "))

valor_a_aumentar = salario * (aumento / 100)
novo_salario = salario + valor_a_aumentar

print(f"Seu salário anterior de {salario}, agora com um aumento de {aumento}, irá para: ")
print("R$ %.2f" % novo_salario)