import os

extensions = {}
current_file = __file__
dir_name = os.path.dirname(current_file)

for file_name in os.listdir(dir_name):
    name, extension = file_name.split('.')
    if extension not in extensions:
        extensions[extension] = []
    extensions[extension].append(file_name)

with open('extensions.txt', 'w') as file:
    for k, v in extensions.items():
        file.write(f'.{k}' + '\n')
        for el in v:
            file.write(f'- - - {el}' + '\n')
