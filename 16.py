# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

a = int(input("Insira o primeiro número: "))

if (a == 0):
    print("Valor Inválido!")
    exit()
else:
    b = int(input("Insira o segundo número: "))
    c = int(input("Insira o terceiro número: "))

delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print("Não possui raízes reais")
    exit()

if (delta == 0):
    x1 = (-b + math.sqrt(delta)) / 2 * a
    print(f"Possui apenas uma raiz real: {x1}")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(f"Possui duas raízes reais: {x1} e {x2}")
