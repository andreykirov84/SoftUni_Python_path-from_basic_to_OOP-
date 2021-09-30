path = input().split('\\')
name = path[-1].split('.')[0]
extension = path[-1].split('.')[1]
print(f'File name: {name}')
print(f'File extension: {extension}')
