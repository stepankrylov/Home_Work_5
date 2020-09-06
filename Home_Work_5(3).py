with open('HW_5(3).txt', 'r', encoding='utf-8') as f:
    payroll = 0
    staff = 0
    print(f'Сотрудники, получающие менее 20 тыс. руб.:')
    for line in f:
        staff += 1
        name = " ".join(line.split()[0:3])
        salary = int(line.split()[3])
        payroll += salary
        if salary < 20000:
            print(f'{name}')
    average_wage = payroll/staff
    print(
          f'\nЗарплатный фонд {payroll} руб.\n'
          f'Кол-во сотрудников {staff} человек\n'
          f'Средний оклад сотрудников составляет {average_wage} руб.'
         )
