number_a = int(input("Digite o valor de A: "))
number_b = int(input("Digite o valor de B: "))
number_c = int(input("Digite o valor de C: "))

def equacao(a, b, c):
    return (b**2) - 4 * (a * c)

delta = equacao(number_a, number_b, number_c)
print("O Delta da equação, com valores de: ")
print(f"A = {number_a}")
print(f"B = {number_b}")
print(f"C = {number_c}")
print(f"É de: {delta}")
