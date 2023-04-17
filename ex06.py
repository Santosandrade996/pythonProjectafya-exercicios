# Notas parciais do aluno:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('o aluno está Aprovado!')
elif media < 5:
    print('O aluno está Reprovado!')
elif media >= 7:
    print('APROVADO COM DISTINÇÃO!')