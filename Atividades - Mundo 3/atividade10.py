valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    print()
    resp = str (input('Quer contnuar?[S/N] ')).strip().upper()[0]
    while resp not in ('S', 'N'):
        print()
        resp = str(input('Resposta inválida!\nQuer continuar [S/N] ')).strip().upper()[0]
    print()
    if resp == 'N':
        break
print('-=--=-' * 10)
print()
print(f'Você digitou os valores {valores} ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista! ')
print()