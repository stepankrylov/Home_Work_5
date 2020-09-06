with open('HW_5(5).txt', 'w') as f:
    f.write(input('Введите числа через пробел: '))

with open('HW_5(5).txt', 'r') as f:
    for line in f:
        print(f'Сумма чисел равна {sum([int(i) for i in line.split()])}')
