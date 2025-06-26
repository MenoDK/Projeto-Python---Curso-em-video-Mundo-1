dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preço = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {preço:2.2f}.')
