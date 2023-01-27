# Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

primeiroProduto = float(input("Insira o primeiro preço: "))
segundoProduto = float(input("Insira o segundo preço: "))
terceiroProduto = float(input("Insira o terceiro preço: "))

if ((primeiroProduto < segundoProduto) and (primeiroProduto < terceiroProduto)):
    print("Primeiro produto é o mais barato")
elif ((primeiroProduto > segundoProduto) and (segundoProduto < terceiroProduto)):
    print("Segundo produto é o mais barato")
else:
    print("Terceiro produto é o mais barato")
