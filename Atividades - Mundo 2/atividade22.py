somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA ----- ')
    nome= str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    somaidade += idade
    sexo = str(input('Sexo [M/F]: ')).strip()
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho} ')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos ')