print('-=--=-' * 10)
print('EX4')

pessoas = {'nome': 'Davi', 'sexo': 'M', 'idade': 20,}

print()
print(pessoas)
print('-' * 60)

print()
print(f'o {pessoas['nome']} tem {pessoas['idade']} anos.')
print('-' * 60)
 
print()
print(pessoas.keys())
print('-' * 60)

print()
print(pessoas.items())
print('-' * 60)

print() 
print(pessoas.values())
print('-' * 60)

print()
for k in pessoas.keys():
    print(k)
print('-' * 60)

print()
for k in pessoas.values():
    print(k)
print('-' * 60)

print()
for k in pessoas.items():
    print(f'{k[0]} = {k[1]}')
print('-' * 60)

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

print()
print(pessoas)
print()
print('-' * 60)
