def value_key_sorted_dict(dd):
    return sorted(dd.items(), key=lambda x: (x[0]))


company_dict = {}
command = input().split(' -> ')
while command[0] != 'End':
    company = command[0]
    employee = command[1]
    if company not in company_dict:
        company_dict[company] = [employee]
        command = input().split(' -> ')
    else:
        if employee not in company_dict[company]:
            company_dict[company] += [employee]
            command = input().split(' -> ')
        else:
            command = input().split(' -> ')

company_dict = dict(value_key_sorted_dict(company_dict))


for company in company_dict:
    print(f'{company}')
    for emp_id in company_dict[company]:
        print(f'-- {emp_id}')
