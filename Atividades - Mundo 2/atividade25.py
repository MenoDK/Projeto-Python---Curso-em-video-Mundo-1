n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print(''' [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    opçao = int(input('>>>> Qual é a sua opção?! '))
    if opçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma} ')
    elif opçao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} X {n2} é {produto} ')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior} ')
    elif opçao == 4:
        print('Informe os números novamente ')
        n1 = int(input('Primeiro valor'))
        n2 = int(input('Segundo valor '))
    elif opçao == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida. Tente novamente ')
    print('=-=' * 10 )
print('Fim do programa! Volte sempre! ')