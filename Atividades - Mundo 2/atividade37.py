total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do PROGRAMA '))
print(f'O total da sua compra foi R${total:.2f}')
print(f'Temos {totmil} produtos caustando mais de 1000R$')
print(f'O produto mais barato foi {barato} que Custa R${menor:.2f}')
