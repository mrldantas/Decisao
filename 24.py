# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

primeiroNumero = float(input("Insira o primeiro número: "))
segundoNumero = float(input("Insira o segundo número: "))
operacao = input("Digite a operação que deseja realizar: ")


def checar():
    if (resultadoOperacao % 1 == 0):
        print("Inteiro")
        if (resultadoOperacao % 2 == 0):
            print("Par")
            if (resultadoOperacao > 0):
                print("Positivo")
            else:
                print("Negativo")
        else:
            print("Impar")
    else:
        print("Decimal")


if (operacao == "+"):
    resultadoOperacao = primeiroNumero + segundoNumero
    print(f"Resultado: {resultadoOperacao}")
    checar()
elif (operacao == "-"):
    resultadoOperacao = primeiroNumero - segundoNumero
    print(f"Resultado: {resultadoOperacao}")
    checar()
elif (operacao == "*"):
    resultadoOperacao = primeiroNumero * segundoNumero
    print(f"Resultado: {resultadoOperacao}")
    checar()
elif (operacao == "/"):
    resultadoOperacao = primeiroNumero / segundoNumero
    print(f"Resultado: {resultadoOperacao}")
    checar()
else:
    print("Valor Inválido")
