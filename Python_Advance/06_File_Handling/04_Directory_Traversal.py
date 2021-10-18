import os

result = {}
for filename in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), filename)):
        print(filename)
        name, extension = filename.split('.')
        print(name, extension)
        if extension not in result.keys():
            result.update({extension: [name]})
        else:
            result[extension].append(name)

print(result)
result = dict(sorted(result.items(), key=lambda x: (x[0], x[1])))
print(result)
for key, value in result.items():
    print(f'.{key}')
    for fname in value:
        print(f'- - - {fname}.{key}')

report_file_name = 'report.xtx'

with open(report_file_name, 'w') as file:
    for key, value in result.items():
        file.write(f'.{key}\n')
        for fname in value:
            file.write(f'- - - {fname}.{key}\n')





