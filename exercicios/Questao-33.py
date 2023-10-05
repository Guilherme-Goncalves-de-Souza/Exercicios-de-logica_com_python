valorCasa = float(input('Digite o valor da casa:'))
salario = float(input('Digite o salário do comprador:'))
anosPagar = int(input('Digite em quantos anos será pago: '))

valorPrestacao = (valorCasa / (anosPagar * 12))
porcentagemSalario = salario * 0.30

if (valorPrestacao > porcentagemSalario):
    print('Empréstimo NEGADO, excedeu os 30% do salário!')
else:
    print('Empréstimo APROVADO, NÃO excedeu os 30% do salário!')