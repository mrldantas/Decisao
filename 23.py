# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Insira um número qualquer: "))

if (numero % 1 == 0):
    print("Inteiro")
else:
    print("Decimal")
