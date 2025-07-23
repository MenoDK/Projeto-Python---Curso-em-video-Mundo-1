aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['Média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-=--=-' * 10)
for k, v in aluno.items():
    print(f'  -  {k} é igual a {v}')