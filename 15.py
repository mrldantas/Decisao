# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

primeiro = float(input("Insira o primeiro lado: "))
segundo = float(input("Insira o segunda lado: "))
terceiro = float(input("Insira o terceiro lado: "))

if (primeiro + segundo < terceiro) or (primeiro + terceiro < segundo) or (segundo + terceiro < primeiro):
    print("Não é um triângulo")
if ((primeiro == segundo) and (primeiro == terceiro)):
    print("Triângulo Equilátero")
if ((primeiro == segundo) and (primeiro != terceiro)):
    print("Triângulo Isósceles")
if ((primeiro != segundo) and (primeiro != terceiro)):
    print("Triângulo Escaleno")
