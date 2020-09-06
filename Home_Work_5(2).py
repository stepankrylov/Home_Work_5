with open('HW_5(2).txt', 'r', encoding='utf-8') as f:
    n = 0
    for line in f:
        n += 1
        print(f'Строка № {n}: "{line.strip()}" | количество слов в строке: {len(line.split())}')
    print(f'Общее кол-во строк в файле: {n}')
