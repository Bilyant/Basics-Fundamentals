directory = input().split('\\')
data = directory[-1].split('.')
file_name, extention = data[0], data[1]
print(f'File name: {file_name}')
print(f'File extension: {extention}')
