numeros = []
while True:
    n = int(input('Digite um valor: ')) 
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adiicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in ('S', 'N'):
        r = str(input("Resposta inválida!\nQuer continuar? [S/N] ")).strip().upper()[0]
    if r == 'N':
        break
print()
print('-=--=-'*10)
numeros.sort()
print(f'Você digitou os valores {numeros}')
print()