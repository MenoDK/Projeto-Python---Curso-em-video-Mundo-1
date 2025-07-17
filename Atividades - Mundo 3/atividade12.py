expr = str(input('Digte uma expressão: ')).strip()
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print()
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print()
    print('Sua expressão está inválida!')
print()