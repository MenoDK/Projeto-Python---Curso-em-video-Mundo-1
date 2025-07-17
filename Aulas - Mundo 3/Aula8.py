print('-=--=-' *10)
print('EX1')
print()
teste = []
teste.append('Davi')
teste.append(27)
galera = []
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print()

print('-=--=-' * 10)

print('EX2')
print()
teste = []
teste.append('Davi')
teste.append(27)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print()