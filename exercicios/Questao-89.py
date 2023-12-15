def borda(numero):
    if(numero == 1):
        print('+-------=======------+')
    elif(numero == 2):
        print('~~~~~~~~:::::::~~~~~~~')
    elif(numero == 3):
        print('<<<<<<<<------->>>>>>>')
    else:
        print('-- Número de borda inválido!')

def gerador(mensagem, numeroVez, numeroBorda):
    borda(numeroBorda)
    for i in range(numeroVez):
        print(f'  {mensagem}')
    borda(numeroBorda)

gerador('Aprendendo PYTHON', 3, 1)