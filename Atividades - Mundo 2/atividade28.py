print('Gerador de PA ')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão do PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} =>', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?!\n (Digite 0 para finalizar o programa) :'))
print(f'Progressão finalizada com {total}')         