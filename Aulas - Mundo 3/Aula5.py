print('EX1')
num = [2 , 5 , 9 , 1]
print() 
print(num)
print() 

print('-=--=-'*10)
print('EX2')
num = [2 , 5 , 9 , 1]
num[2] = 3
print() 
print(num)
print() 

print('-=--=-'*10)
print('EX2')
num = [2 , 5 , 9 , 1]
num[2] = 3
num.append(7)
print() 
print(num)
print() 

print('-=--=-'*10)
print('EX3')
num = [2 , 5 , 9 , 1]
num[2] = 3
num.append(7)
num.sort()
print() 
print(num)
print() 

print('-=--=-'*10)
print('EX4')
num = [2 , 5 , 9 , 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
print() 
print(num)
print() 

print('-=--=-'*10)
print('EX5')
num = [2 , 5 , 9 , 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print() 
print(num)
print()
print(f'Essa lista tem {len(num)} elementos.')

print('-=--=-'*10)
print('EX6')
num = [2 , 5 , 9 , 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
print()
print(num)
print()
print(f'Essa lista tem {len(num)} elementos. ')

print('-=--=-'*10)
print('EX7')
num= [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
print()
print(num)
print()
print(f'Essa lista tem {len(num)} elementos. ')

print('-=--=-'*10)
print('EX8')
num2 = [2, 5, 9, 1]
num2[2] = 3
num2.append(7)
num2.sort(reverse=True)
num2.insert(2, 0)
num2.pop(2)
print()
print(num2)
print()
print(f'Essa lista tem {len(num2)} elementos. ')

print('-=--=-'*10)
print('EX9')
num3 = [2, 5, 9, 1]
num3[2] = 3
num3.append(7)
num3.sort(reverse=True)
num3.insert(2, 2)
num3.remove(2)
print()
print(num3)
print()
print(f'Esse lista tem {len(num3)} elementos.')

print('-=--=-'*10)
print('EX10')
num4 = [2, 5, 9, 1]
num4[2] = 3
num4.append(7)
num4.sort(reverse=True)
num.insert(2, 2)
if 4 in num4:
    num.remove(4)
else:
    print()
    print('Não achei o número 4')
    print()
print()
print(num4)
print()
print(f'Essa lista tem {len(num)} elementos. ')

print('-=--=-'*10)
print('EX10')
num5 = [2, 5, 9, 1]
num5[2] = 3
num5.append(7)
num5.sort(reverse=True)
num5.insert(2, 2)
if 5 in num5:
    num.remove(5)
else:
    print()
    print('Não achei o número 5')
    print()
print()
print(num5)
print()
print(f'Essa lista t em {len(num)} elementos')