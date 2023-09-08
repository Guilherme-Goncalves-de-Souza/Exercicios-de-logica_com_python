number_1 = int(input("Digite o PRIMEIRO número inteiro: "))
number_2 = int(input("Digite o SEGUNDO número inteiro: "))

if(number_1 > number_2):
    print(f"O primeiro valor ({number_1}) é MAIOR que o segundo valor ({number_2})")
elif(number_2 > number_1):
    print(f"O segundo valor ({number_2}) é MAIOR que o primeiro valor ({number_1})")
else:
    print(f"Os valores {number_1, number_2} são iguais!")

