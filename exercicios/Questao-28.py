largura = float(input("Digite a largura em m²: "))
comprimento = float(input("Digite o comprimento em m²: "))

area = largura * comprimento

print("Classificações:")
print("- Abaixo de 100m² = TERRENO POPULAR ")
print("- Entre 100m² e 500m² = TERRENO MASTER ")
print("- Acima de 500m² = TERRENO VIP ")
print("----------------------------------------")

print(f"Seu terreno com {area} m² é: ")

if(area < 100):
    print("TERRENO POPULAR")
elif(area >= 100 and area <= 500):
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")