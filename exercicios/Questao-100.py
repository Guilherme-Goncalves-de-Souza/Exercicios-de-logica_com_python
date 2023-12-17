def Media(n1, n2):
    media = (n1 + n2) / 2
    return media

def Situacao(media):
    if(media >= 70):
        return 'APROVADO'
    elif(media >= 50 and media < 70):
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'

nota1 = float(input('Digite a 1° nota (de 0 a 100): '))
nota2 = float(input('Digite a 2° nota (de 0 a 100): '))

mediaFinal = Media(nota1, nota2)
situacaoFinal = Situacao(mediaFinal)
print(f'A média das notas {nota1} e {nota2} foi de {mediaFinal: .2f}!')
print(f'Com isso o aluno está: {situacaoFinal}!')