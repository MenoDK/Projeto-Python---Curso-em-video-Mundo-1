distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você esta preste s a começar uma viagem de {distancia}KM')
if distancia <= 200:
    preço = distancia * 0.5
else: 
    preço = distancia * 0.45
print(f' E o preço da sua passagem será de R${preço:.2f}')
