temp = []
princ = []
mai = men = 0
while True:
    print('-=--=-' *10)
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    print('-=--=-' * 10)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp and resp[0] in 'SN':
            resp = resp[0]
            break
        print('Opção inválida! Digite S ou N!!')
    if resp == 'N':
        break
print('-=--=-' * 10)
print('Os dados cadastrados:')
for pessoa in princ:
    print(f'Nome: {pessoa[0]}, Peso: {pessoa[1]} kg')
print()
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print()
print(f'O maior peso foi de {mai} kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {men} kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()
print('-=--=-' * 10)
print()