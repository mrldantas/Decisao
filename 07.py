# Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro = int(input('Insira o primeiro numero: '))
segundo = int(input('Insira o segundo numero : '))
terceiro = int(input('Insira o terceiro numero: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print(f"Maior: {maior}")

menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print(f"Menor: {menor}")
