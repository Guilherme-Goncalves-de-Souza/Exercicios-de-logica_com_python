media_1 = float(input("Digite a primeira nota: "))
media_2 = float(input("Digite a segunda nota: "))
soma = media_1 + media_2
count = 2

def media(media, contador):
    media_final = media / contador
    return media_final


while True:
    print(" ----------------------- ")
    print("1-  Adicionar mais notas ")
    print("2-  Não adicionar mais  ")
    print(" ----------------------- ")
    menu = int(input("-> "))

    # --------------------------------------

    if(menu == 1):
        nova_media = float(input("Digite a próxima nota: "))
        soma += nova_media
        count += 1
        continue

    elif(menu == 2):
        media_final = media(soma, count)
        print(f"A média entre os {count} números é de: {media_final}")
        break

    else:
        print("Digite um número válido!")
        continue