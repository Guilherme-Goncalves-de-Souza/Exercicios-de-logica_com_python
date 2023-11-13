import random
import time

print("!Descubra o valor!")
print("-" * 20)

print("Sorteando valor...")
valor_computador = random.randint(1, 10)
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("Valor sorteado!")
print("-" * 20)

print("Agora sua vez de tentar descobrir o número de 1 a 10: ")

for i in range(1, 5, 1):
    print(f'{i}° tentativa:')
    print('-----------')
    valor_jogador = int(input("-> "))

    if (valor_jogador > 0 and valor_jogador <= 10):
        print("=" * 20)

        print(f"Valor do ESCOLHIDO: {valor_jogador}")

        if (valor_computador == valor_jogador):
            print(f"Você ACERTOOOOUUUUUUU! de {i}°!")
            break
        else:
            if(i != 4):
                print(":( Não foi dessa vez, tente novamente!")
            else:
                print(':( Não foi dessa vez!')
                print('-----!TENTATIVAS ESGOTADAS!-----')
                print(f'O número sorteado era o -> {valor_computador}.')
                print('Tente novamente na próxima partida!')

    else:
        print("Digite um valor válido de 1 a 10!")