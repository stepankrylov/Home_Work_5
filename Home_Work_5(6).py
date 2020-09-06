import re

dict_course = {}
with open('HW_5(6).txt', 'r', encoding='utf-8') as f:
    for line in f:
        list_num = sum([int(i) for i in re.findall(r'[0-9]+', line)])
        dict_course[line.strip().split()[0][:-1]] = list_num
    print(dict_course)
