galera = []
pessoa = {}
soma = media = 0

print('-=--=-' * 10)

while True:
    print()
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Error! Por favor, digite M ou F. ')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    print()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in  'SN':
            break
        print('Error! Responda com S ou N.')

    if resp == 'N':
        break

print()
print('-=--=-' * 10)

print()
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas. ')

media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos. ')

print('C) As mulheres cadastradas foram ', end ='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'"{p["nome"]} "', end='')

print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k:<6} = {v}') 
        print() 

print()
print('>> ENCERRRADO <<')
print()
print('-=--=-' * 10)
print()