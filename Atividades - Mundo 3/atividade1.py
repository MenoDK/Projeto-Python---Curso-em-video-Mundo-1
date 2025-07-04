cont = ('zero','um' , 'dois' , 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze' , 'doze', 'treze' , 'catorze', 'quinze', 'dezesseis', 'dezessete' , 'dezoito', 'dezenove', 'vinte')
resp = 'S'
while resp == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cont[num]}')
    resp = input('Quer continuar? [S/N]: ').strip().upper()