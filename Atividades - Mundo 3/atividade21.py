from datetime import datetime 
print('-=--=-' * 10)
print() 

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now() .year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
else:
    print(f"{dados['nome']} não possui carteira de trabalho.")

print()
print('-=--=-' * 10)

for k, v in dados.items():
    if k == 'salário':
        print(f'   - {k}: R${v}')
    else:
        print(f'   - {k}: {v}')

print('-=--=-' * 10)
print()