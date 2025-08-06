from uteis1 import fatorial, dobro, triplo, linha

linha()

num = int(input('Digite um valor: '))
fat = fatorial(num)

linha()
print(f'O fartorial de {num} é = {fat} ')

linha()
print(f' O dobro de {num} é = {dobro(num)} ')

linha()
print(f' O triplo de {num} é = {triplo(num)} ')

linha()