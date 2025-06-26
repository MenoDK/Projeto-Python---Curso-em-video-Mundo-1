preço = float(input('Digite o preço do produto: R$ '))
novo = preço  - (preço * 5 / 100)
print(f'O produto que custava R$ {preço:.2f}, na promoção com 5% de desconto, vai custar R$ {novo:.2f}.')