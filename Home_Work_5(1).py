with open('HW_5(1).txt', 'a') as f:
    while True:
        x = input('Введите строку: ')
        if x != '':
            f.write(x + '\n')
        else:
            break
