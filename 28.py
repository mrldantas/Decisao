# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = input("Insira qual carne você irá comprar: ")
peso = float(input("Quantidade da carne em kg: "))
cartao = input("O pagamento será no cartão Tabajara? ")

precoFile1 = peso * 4.9
precoFile2 = peso * 5.8

precoAlcatra1 = peso * 5.9
precoAlcatra2 = peso * 6.8

precoPicanha1 = peso * 6.9
precoPicanha2 = peso * 7.8

if (carne == "File Duplo"):
    if (peso < 5):
        precoTotal = precoFile1
    else:
        precoTotal = precoFile2

if (carne == "Alcatra"):
    if (peso < 5):
        precoTotal = precoAlcatra1
    else:
        precoTotal = precoAlcatra2

if (carne == "Picanha"):
    if (peso < 5):
        precoTotal = precoPicanha1
    else:
        precoTotal = precoPicanha2

if (cartao == "Sim"):
    print(f"Tipo: {carne}")
    print(f"Quantidade: {peso}kg")
    print(f"Preço total: {precoTotal} reais")
    print("Pagamento: Cartão Tabajara")
    print("Desconto: 5%")
    print(f"Valor final: {precoTotal * 0.95} reais")
elif (cartao == "Não"):
    print(f"Tipo: {carne}")
    print(f"Quantidade: {peso}kg")
    print(f"Preço total: {precoTotal:.2f} reais")
    print("Pagamento: À vista")
    print("Desconto: Nenhum")
    print(f"Valor final: {precoTotal:.2f} reias")
