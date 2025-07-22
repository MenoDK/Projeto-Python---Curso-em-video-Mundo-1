print('-=--=-' * 10)
print('EX6')
print()
estado = {}
brasil = []
for c in range(0,3):
    estado['uf']= str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    print()
    brasil.append(estado.copy())

print('-=--=-' * 10)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

print('-=--=-' * 10)
print()