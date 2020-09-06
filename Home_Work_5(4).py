dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('HW_5(4).txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = line.strip().split()
        el_dict = dict_num[line.strip().split()[0]]
        line_list[0] = el_dict
        line_str = ' '.join(line_list)
        with open('HW_5(4)_new.txt', 'a', encoding='utf-8') as file:
            print(line_str)
            file.write(line_str + '\n')
