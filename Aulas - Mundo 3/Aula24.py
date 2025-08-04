def somar(a= 0, b= 0, c= 0):
    s = a + b + c 
    return s


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()



r1 = somar(3, 2, 5)
r2 = somar(2, 3)
r3 = somar(2)
r4 = somar()

linha()
print(f'Meus cálculos deram {r1}, {r2} e {r3}. ')

linha()