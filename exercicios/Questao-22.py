ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2023 - ano_nascimento

if(idade == 18):
    print("Você deve se alistar esse ano!")

elif(idade > 18):
    print(f"Você deveria ter se alistado a {idade - 18} anos atrás!")

else:
    print(f"Você deverá se alistar daqui à {18 - idade} anos")