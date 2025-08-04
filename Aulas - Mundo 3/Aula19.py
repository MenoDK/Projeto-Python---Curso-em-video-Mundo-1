def contador(i, f, p):
    """--- > Faz uma Contagem e mostra na tela"
    "i = Início "
    "f = fim da Contagem"
    "p = Passo da Contagem
    return: Sem Retorno
     Função criada por DK < --- """
    c = i
    while c <= f:
        print(f'{c}', end= '..')
        c += p
    print('FIM')

def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()

linha()
contador(2, 10, 2)
linha()
contador(0, 100, 10)
linha

help(contador)

linha()

help(linha)

linha()
