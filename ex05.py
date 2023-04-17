# Calculando o salário no referido mês:
ganha_hora = float(input('Digite o quanto se ganha por hora de trabalho?'))
horas_trabalho = int(input('Digite a horas trabalhadas no mês: '))
salario_bruto = ganha_hora * horas_trabalho
ir = (11 * salario_bruto / 100)
inss = (8 * salario_bruto / 100)
sindicato = (5 * salario_bruto / 100)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print('')
print('----------salário------------')
print('Salário bruto.............................: R${:.2f}'.format(salario_bruto))
print('INSS.................................: R${:.2f}'.format(inss))
print('Sindicato...................................: R${:.2f}'.format(sindicato))
print('Salário liquido.........................................: R${:.2f}'.format(salario_liquido))
print('')
