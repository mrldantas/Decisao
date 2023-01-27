# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Insira o combustivel (A para alcool e G para gasolina): ")
listrosVendidos = float(input("Insira quantos litros foram vendidos: "))
precoGasolina = 2.5
precoAlcool = 1.9

if (combustivel == "A"):
    if (0 < listrosVendidos <= 20):
        print(f"Valor com desconto {listrosVendidos * 1.85:.2f} reais")
    else:
        print(f"Valor com desconto {listrosVendidos * 1.8:.2f}reais")

elif (combustivel == "G"):
    if (0 < listrosVendidos <= 20):
        print(f"Valor com desconto {listrosVendidos * 2.4:.2f} reais")
    else:
        print(f"Valor com desconto {listrosVendidos * 2.35:.2f} reais")
