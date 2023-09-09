reta1 = float(input("Digite o tamanho do PRIMEIRO segmento de reta: "))
reta2 = float(input("Digite o tamanho do SEGUNDO segmento de reta: "))
reta3 = float(input("Digite o tamanho do TERCEIRO segmento de reta: "))

condicao_1 = (reta2 + reta3) > reta1
condicao_2 = (reta1 + reta3) > reta2
condicao_3 = (reta1 + reta2) > reta3

if(condicao_1 and condicao_2 and condicao_3):
    print(f"Será SIM possível formar um triângulo com os comprimento de: {reta1, reta2, reta3}")

    if(reta1 == reta2 == reta3):
        print("O triângulo será EQUILÁTERO, ou seja, tem todos os lados iguais.")
    elif(reta1 == reta2  or reta1 == reta3 or reta2 == reta3):
        print("O triângulo será ISÓSCELES, ou seja, tem 2 lados iguais.")
    else:
        print("O triângulo será ESCALENO, ou seja, todos os lados são diferentes.")


else:
    print(f"NÃO será possível formar um triângulo com os comprimentos de: {reta1, reta2, reta3}")