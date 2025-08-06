def ficha(jogador= '<desconhecido>', gol=0):
    linha()
    print(f' O jogador {jogador} fez {gol} gols(s) no campeonato. ')


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()

linha()
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)


linha()
