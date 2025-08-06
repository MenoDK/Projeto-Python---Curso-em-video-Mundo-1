def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            linha()
        if ok:
            break
    return valor


def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()

linha()    
n = leiaInt('Digite um número: ')

print()
print(f'Você acabou de digitar o número {n}. ')

linha()