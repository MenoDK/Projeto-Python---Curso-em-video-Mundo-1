def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'com {idade} anos: NÃO VOTA. '
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL. '
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO. '
    
def linha():
    """Faz uma linha para separar melhor as respostas do sistema"""
    print()
    print('-=--=-' * 10)
    print()

linha() 
nasc = int(input(' Em que ano você nasceu?! '))

print()
print(voto(nasc))
linha()