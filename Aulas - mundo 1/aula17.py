nome = 'Davi'
print(f' Olá!!! Muito prazer em te conhecer, \033[4;34m{nome}\033[4;34m!!\033[m')

nome = 'Davi'
cores = {'limpa':'\033[m', 'azul' : '\033[34m', 'amarelo' : '\033[33m', 'pretoebranco' : '\033[7;37m'}
print(f' Olá!!! Muito prazer em te conhecer, {(cores['pretoebranco'])} {nome} {(cores['limpa'])}!!')