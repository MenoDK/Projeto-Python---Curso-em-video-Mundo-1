velocidade = float (input ('Qual é a velocidade atual do carro? '))
if velocidade > 90:
    print(' MULTADO! Você excedeu o limite permitod que é 80km/h')
    multa = (velocidade-80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')