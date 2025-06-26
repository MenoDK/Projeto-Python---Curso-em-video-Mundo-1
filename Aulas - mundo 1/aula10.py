frase = 'Curso em Video Python '
print(frase.upper().count('O'))
print(frase.lower().count('o'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('video'))
print(frase.lower().find('video'))

dividido = frase.split()
print(dividido[2] [3])