nota1 = int(input("Digite a PRIMEIRA nota: "))
nota2 = int(input("Digite a SEGUNDA nota: "))

media = (nota1 + nota2) / 2

if(media < 4.9 or media < 49):
    print("Com a média de %.2f, Aluno REPROVADO!" % media)
elif((media >= 5.0 and media <= 6.9) or (media >= 50 and media <= 69)):
    print("Com a média de %.2f, Aluno de RECUPERAÇÃO!" % media)
elif(media >= 7 or media >= 70):
    print("Com a média de %.2f, Aluno APROVADO!" % media)
