def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()


linha()   
num = int(input('Digite um número: '))
print()

if par(num):
    print('É par! ')
else:
    print('Não é par')

linha()