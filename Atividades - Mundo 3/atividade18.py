ficha = []
print('-=--=-' * 10)
print()
print('      MÉDIA ALUNOWS      '.center(60))
print()
while True:
    print('-=--=-' * 10)
    nome = str(input('Nome:')).strip()
    nota1 = float(input('Nota 1: ').replace(',', '.'))
    nota2 = float(input('Nota 2: ').replace(',', '.'))
    print('-=--=-' * 10)
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while resp not in 'SN':
        respe = str(input('Opção inválida!\nDigite S ou N: ')).strip().upper()[0]
        print('-=--=-' * 10)
    if resp in 'N':
        break
print('-=--=-' * 10)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
print('------' * 10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    print('------' * 10)
while True:
    opc = int(input('Mostrar notas de qual aluno? (Digite o seu "No.")\n999 interrompe \nR: '))
    print()
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc < len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
        print()
        print('-=--=-' * 10)
print()
print('<<< VOLTE SEMPRE >>>')
print()
print('-=--=-' * 10)
print()