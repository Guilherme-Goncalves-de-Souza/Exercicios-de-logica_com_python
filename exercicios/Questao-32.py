import random
import time

print("!Descubra o valor!")
print("-" * 20)

print("Sorteando valor...")
valor_computador = random.randint(1, 5)
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("Valor sorteado!")
print("-" * 20)

print("Agora sua vez de tentar descobrir o número de 1 a 5: ")
valor_jogador = int(input("-> "))
if(valor_jogador > 0 and valor_jogador <= 5):
    print("=" * 20)

    print(f"Valor do SORTEADO: {valor_computador}")
    print(f"Valor do ESCOLHIDO: {valor_jogador}")

    if(valor_computador == valor_jogador):
        print("Você ACERTOOOOUUUUUUU!")
    else:
        print("Não foi dessa vez, você ERROOOOUUUU!")

else:
    print("Digite um valor válido de 1 a 5!")