import json

list_profit = []
dict_firm = {}
with open('HW_5(7).txt', 'r', encoding='utf-8') as f:
    for line in f:
        firm = line.strip().split()
        name = firm[0]
        ownership = firm[1]
        revenue = int(firm[2])
        cost = int(firm[3])
        profit = revenue - cost
        if profit >= 0:
            list_profit.append(profit)
        dict_firm[name] = profit

    average_profit = sum(list_profit)/len(list_profit)
    print(f'Среднее значение прибыли составляет {average_profit} руб.')
    result = [dict_firm, {'average_profit': average_profit}]
    print(result)

    with open("firm.json", "w") as write_f:
        json.dump(result, write_f)
