quantidade_cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Digite quantos anos você já fuma: "))

dias_perdidos = (quantidade_cigarros * (anos_fumados * 365)) * 0.0069

print("A quantidade de dias que você perdeu foram de: %.0f" % dias_perdidos)