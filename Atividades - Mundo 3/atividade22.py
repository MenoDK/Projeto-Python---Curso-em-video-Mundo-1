jogador = {}
partidas = []

print('-=--=-' * 10)

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou?! '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partidas {c} ? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print()
print('-=--=-' * 10)

for k, v in jogador.items():
    if k == 'gols':
        print(f"{k}: {', '.join(str(g) for g in v)} gols")
    else:
        print(f'{k}: {v}')

print()
print('-=--=-' * 10)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')

print()
print('-=--=-' * 10)

print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador['total']} gols')

print('-=--=-' * 10)
print()
 