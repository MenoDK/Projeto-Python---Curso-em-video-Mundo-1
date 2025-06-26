nome = input('Qual o seu nome? ')
print('É um prazer te conhecer {:20}!'.format(nome))

nome = input('Qual o seu nome? ')
print(f'É um prazer te conhecer ¨{nome:20}!')

nome = input('Qual o seu nome? ')
print(f'É um prazer te conhecer ¨{nome:>20}!')

nome = input('Qual o seu nome? ')
print(f'É um prazer te conhecer ¨{nome:<20}!')

nome = input('Qual o seu nome? ')
print(f'É um prazer te conhecer ¨{nome:=^20}!')

nome = str(input('Qual o seu nome? '))
print(f'É um prazer te conhecer ¨{nome:=^20}!')