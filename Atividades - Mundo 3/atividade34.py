def notas(*n, sit=False):
    """---- > Função para analisar notas e situação de vários alunos. 
    :param n: uma ou mais notas dos alunos (aceita várias) 
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma. """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] >= 5
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()


resp = notas(10, 3.5, 5.5, sit=True)
linha()

print(resp)
linha()

help(notas)
linha()