def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} X {comp} é de {a}m² ')

def linha():
    print()
    print('-=--=-' * 10)
    print()


linha()


print(' Controle de Terrenos ')

linha()


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))


linha()


área(l, c)


linha()