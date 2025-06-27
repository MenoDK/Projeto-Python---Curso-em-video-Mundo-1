num = int(input('Digite um número inteiro:'))
print('-----'*20)
print('''Ecolha uma das bases para conversão:
[  1  ] converter para BINÁRIO
[  2  ] Converter para OCTAL
[  3  ] Converter para HEXADECIMAL''')
print('-----'*20)
opçao = int(input('Sua opção: '))
if opçao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente')