def somar(a=0, b=0, c = 0):
    """ --- > Faz a soma de 3 valores e mostra o resultado na tela
    a = primeiro valor
    b = segundo valor 
    c terceiro valor
    Função criada por DK < --- """
    s = a + b + c
    print(f'A soma vale: {s} ')


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()

linha()

somar(3, 2, 5)
linha()

somar(8, 4)
linha()

somar(3)
linha()

somar()
linha()

somar(b=4, c=2)
linha()
