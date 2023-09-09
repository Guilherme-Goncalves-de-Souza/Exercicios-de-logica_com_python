nome_func = input("Digite seu nome: ")
salario_func = float(input("Digite seu salário em R$: "))
anos_trab_func = int(input("Digite quantos anos você trabalha na empresa: "))

if(anos_trab_func < 3):
    aumento = salario_func * 0.03
    novo_salario_func = aumento + salario_func
    print(f"{nome_func}, Com um aumento de 3% seu salário de R$ {salario_func}")
    print(f"Irá para: R$ {novo_salario_func}")
elif(anos_trab_func >= 3 and anos_trab_func < 10):
    aumento = salario_func * 0.125
    novo_salario_func = aumento + salario_func
    print(f"{nome_func}, Com um aumento de 12,5%, seu salário de R$ {salario_func}")
    print(f"Irá para: R$ {novo_salario_func}")
else:
    aumento = salario_func * 0.2
    novo_salario_func = aumento + salario_func
    print(f"{nome_func}, Com um aumento de 20%, seu salário de R$ {salario_func}")
    print(f"Irá para: R$ {novo_salario_func}")