print(f"{'loja guanabara':=^40}")
preço = float(input('Preço das compras: R$ '))
print('=-=-=-='*13)
print('''FORMAS DE PAGAMENTO
[  1  ] á vista dinheir/cheque
[  2  ] á vista cartão
[  3  ] 2x no cartão
[  4  ] 3x no cartão ''')
print('=-=-=-='*13)
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2 
    print(f'Sua compra sera parcelada em 2x de R$ {parcela:.2f} SEM JUROS ')
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R$ {parcela:.2f} COM JUROS')
else:
    total = preço
    print('Opção inválida de pagamento. Tente novamente.')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')