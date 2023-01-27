# Faça um Programa que leia três números e mostre-os em ordem decrescente.

primeiroNumero = int(input("Insira o primeiro número: "))
segundoNumero = int(input("Insira o segundo número: "))
terceiroNumero = int(input("Insira o terceiro número: "))

if primeiroNumero < terceiroNumero:
    primeiroNumero, terceiroNumero = terceiroNumero, primeiroNumero

if primeiroNumero < segundoNumero:
    primeiroNumero, segundoNumero = segundoNumero, primeiroNumero

if segundoNumero < terceiroNumero:
    segundoNumero, terceiroNumero = terceiroNumero, segundoNumero

print(f'A ordem decrescente é {primeiroNumero}, {segundoNumero} e {terceiroNumero}')
