sexo = str(input('Informe seu  sexo: [M/F] '))
while sexo not in 'MmFf':
    sexo = str(input('  Dados inválidows. Por favor, informe seu sexo: '))
print(f'Sexo {sexo} registrado com sucesso' )
