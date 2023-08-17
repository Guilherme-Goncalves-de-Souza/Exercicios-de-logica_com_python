ano_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2023 - ano_nascimento

if(idade >= 16):
    print("Você JÁ está apto(a) á votar!")
else:
    idade_faltante_a_votar = 16 - idade
    print(f"Você NÃO está apto(a) á votar, ainda faltam {idade_faltante_a_votar} anos para você votar!")