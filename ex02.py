# Faça um Programa que peça as 4 notas bimestrais e mostre a média
n1 = float(input('Primeiro nota bimestral: '))
n2 = float(input('Segunda nota bimestral: '))
n3 = float(input('Terceira nota bimestral: '))
n4 = float(input('Quarta nota bimestral: '))
m = (n1 + n2 + n3 + n4) / 4
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))
print('E a nota entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n3, n4, m))

