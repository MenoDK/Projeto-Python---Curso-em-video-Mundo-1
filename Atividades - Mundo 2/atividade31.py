resp = 'S'
soma = quant = media = menor = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')