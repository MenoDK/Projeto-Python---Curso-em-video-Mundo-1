time = list()
jogador = dict()
partidas = list()
print('-=--=-' * 10)
while True:
    print()
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou?! '))

    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        print()
        print('-=--=-' * 10)
        resp = str(input('Quer continuar?! [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda com S ou N')
        print('-=--=-' * 10)

    if resp == 'N':
        break
    

print('--' * 30)
print('cod', end=' ')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print()
print('--' * 30)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print()
print('-=--=-' * 10)
print()

while True:
    busca = int(input('Mostrar dados de qual jogador?! (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! Não existe jogador com código {busca}! ')
    else:
        print()
        print(f' -- LEVANTAMENTO DO JOGAR {time[busca] ['nome']}')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'       No jogo{i+1} fez {g} gols')
        print()

print()
print('>>>VOLTE SEMPRE<<< ')
print()
print('-=--=-' * 10)
print()