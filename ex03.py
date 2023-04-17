# Calculando peso para homens e mulheres:
sexo = int(input('Digite o sexo: (1- Feminino, 2- Masculino) '))
altura = int(input('Digite a altura: (em cm) '))
if sexo == 1:
    print('Feminino')
    formula_peso = (62.1 * altura / 100) - 44.7
    print(f'O peso ideal é de {round(formula_peso, 2)} kg')
else:
    print('Masculino')
    formula_peso = (72.7 * altura / 100) - 58
    print(f'O peso ideal é de {round(formula_peso, 2)} kg')
