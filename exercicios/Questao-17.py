velocidade = float(input("Digite a velocidade do carro em km/h:"))

if(velocidade > 80):
    velocidade_acima = velocidade - 80
    valor_multa = velocidade_acima * 5
    print("Você foi multado em R$ %.2f" % valor_multa)

else:
    print("Você está dentro do limite de velocidade, parabéns!!!")