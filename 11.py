# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Insira seu salário: "))

if (salario < 280.01):
    novoSalario = salario * 1.2
    print(f"Seu antigo salário é: {salario} reais")
    print("O percentual de aumento será 20%")
    print(f"O valor do aumento é {novoSalario - salario} reais")
    print(f"Seu novo salario é {salario * 1.2} reais")

if ((salario > 280) and (salario < 701.01)):
    novoSalario = salario * 1.15
    print(f"Seu antigo salário é: {salario} reais")
    print("O percentual de aumento será 15%")
    print(f"O valor do aumento é {novoSalario - salario} reais")
    print(f"Seu novo salario é {salario * 1.15} reais")

if ((salario > 700) and (salario < 1500.01)):
    novoSalario = salario * 1.1
    print(f"Seu antigo salário é: {salario} reais")
    print("O percentual de aumento será 10%")
    print(f"O valor do aumento é {novoSalario - salario} reais")
    print(f"Seu novo salario é {salario * 1.1} reais")

if (salario > 1500):
    novoSalario = salario * 1.05
    print(f"Seu antigo salário é: {salario} reais")
    print("O percentual de aumento será 5%")
    print(f"O valor do aumento é {novoSalario - salario} reais")
    print(f"Seu novo salario é {salario * 1.05} reais")
