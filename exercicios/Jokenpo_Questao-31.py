import random
import time


print("!Bem vindo ao JoKenPO!")
print("-" * 25)

jogadas = ["PEDRA", "PAPEL", "TESOURA"]

print("1- PEDRA")
print("2- PAPEL")
print("3- TESOURA")
print("-" * 25)
print("Vez do COMPUTADOR: ")
number_computador = random.randint(1, 3)
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("-" * 25)
print("SUA vez: ")
number_jogador = int(input("-> "))

if(number_jogador > 0 and number_jogador <= 3):
    print("-" * 25)
    print(f"Jogada do COMPUTADOR: {jogadas[number_computador - 1]}")
    print(f"SUA jogada: {jogadas[number_jogador - 1]}")
    print("=" * 25)
    time.sleep(0.5)

    if(number_computador == 1):
        if(number_jogador == 1):
            print("EMPATE!")
        elif(number_jogador == 2):
            print("Você GANHOU!")
        elif(number_jogador == 3):
            print("Você PERDEU!")

    elif (number_computador == 2):
        if (number_jogador == 1):
            print("Você PERDEU!")
        elif (number_jogador == 2):
            print("EMPATE!")
        elif (number_jogador == 3):
            print("Você GANHOU!")

    elif (number_computador == 3):
        if (number_jogador == 1):
            print("Você GANHOUR!")
        elif (number_jogador == 2):
            print("Você PERDEU!")
        elif (number_jogador == 3):
            print("EMPATE!")

else:
    print("Digite um número válido!")