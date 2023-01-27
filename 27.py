# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

pesoMorango = float(input("Insira a quantidade de morangos em KG: "))
pesoMaca = float(input("Insira a quantidade de maçãs em KG: "))

precoMorango1 = pesoMorango * 2.5
precoMorango2 = pesoMorango * 2.2

precoMaca1 = pesoMaca * 1.8
precoMaca2 = pesoMaca * 1.5

if (pesoMorango < 5):
    precoCertoMorango = precoMorango1
else:
    precoCertoMorango = precoMorango2

if (pesoMaca < 5):
    precoCertoMaca = precoMaca1
else:
    precoCertoMaca = precoMaca2

precoTotal = precoCertoMorango + precoCertoMaca
pesoTotal = pesoMorango + pesoMaca

if ((precoTotal > 25) or (pesoTotal > 8)):
    print(f"O preço final é: {precoTotal * 0.9:.2f} reais")
else:
    print(f"O preço final é: {precoTotal:.2f} reais")
