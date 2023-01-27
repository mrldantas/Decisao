# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Insira a letra desejada (Minúsculo): ")

if ((letra != "a") and (letra != "e") and (letra != "i") and (letra != "o") and (letra != "u")):
    print("Consoante")
else:
    print("Vogal")
