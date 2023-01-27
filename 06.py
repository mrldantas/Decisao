# Faça um Programa que leia três números e mostre o maior deles.

primeiroNumero = int(input("Insira o primeiro numero: "))
segundoNumero = int(input("Insira o segundo numero: "))
terceiroNumero = int(input("Insira o terceiro numero: "))

if ((primeiroNumero > segundoNumero) and (primeiroNumero > terceiroNumero)):
    print("Primeiro número é o maior")
elif ((primeiroNumero < segundoNumero) and (segundoNumero > terceiroNumero)):
    print("Segundo número é o maior")
else:
    print("Terceiro número é o maior")
