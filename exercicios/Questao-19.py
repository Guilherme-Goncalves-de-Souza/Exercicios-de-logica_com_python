nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a 1° nota do aluno: "))
nota2 = float(input("Digite a 2° nota do aluno: "))
media_notas = (nota1 + nota2) / 2

if(media_notas >= 7):
    print("O aluno está aprovado, com a média de: %.2f!" % media_notas)

else:
    print("O aluno está reprovado, com a média de: %.2f!" % media_notas)
