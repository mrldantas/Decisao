# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

horaTrabalhada = int(input("Insira quantas horas você trabalhou: "))
precoHora = int(input("Insira o valor da hora trabalhada: "))

salarioBruto = horaTrabalhada * precoHora

INSS = salarioBruto * 0.1
FGTS = salarioBruto * 0.11
desconto = INSS + FGTS
liquido = salarioBruto - desconto

imposto1500 = salarioBruto * 0.05

imposto2500 = salarioBruto * 0.1

impostoMais2500 = salarioBruto * 0.2

if (salarioBruto < 900.01):
    print(f"Salário Bruto: {salarioBruto} reais")
    print("Imposto de renda: Isento")
    print(f"INSS: {INSS} reais")
    print(f"FGTS: {FGTS} reais")
    print(f"Descontos: {desconto} reais")
    print(f"Salário Líquido: {liquido}")

if (salarioBruto < 1500.01):
    print(f"Salário Bruto: {salarioBruto} reais")
    print(f"Imposto de renda: {imposto1500}")
    print(f"INSS: {INSS} reais")
    print(f"FGTS: {FGTS} reais")
    print(f"Descontos: {desconto} reais")
    print(f"Salário Líquido: {liquido}")

if (salarioBruto < 2500.01):
    print(f"Salário Bruto: {salarioBruto} reais")
    print(f"Imposto de renda: {imposto2500}")
    print(f"INSS: {INSS} reais")
    print(f"FGTS: {FGTS} reais")
    print(f"Descontos: {desconto} reais")
    print(f"Salário Líquido: {liquido}")

if (salarioBruto > 2500):
    print(f"Salário Bruto: {salarioBruto} reais")
    print(f"Imposto de renda: {impostoMais2500}")
    print(f"INSS: {INSS} reais")
    print(f"FGTS: {FGTS} reais")
    print(f"Descontos: {desconto} reais")
    print(f"Salário Líquido: {liquido}")
