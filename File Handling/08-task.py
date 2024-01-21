import os


def file_exists(name):
    it_exists = True
    if not os.path.exists(name):
        it_exists = False
        print('An error occurred')
    return it_exists


line = input()

while line != 'End':
    data = line.split('-')
    command = data[0]
    file_name = data[1]

    if command == 'Create':
        new_file = open(f'{file_name}', 'w').close()

    elif command == 'Add':
        content = data[2]
        with open(f'{file_name}', 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        old_str, new_str = data[2], data[3]
        if file_exists(file_name):
            with open(f'{file_name}') as file:
                new_file = file.read().replace(old_str, new_str)
                file.seek(0)  # returns the cursor at the beginning
                file.truncate()  # deletes all the content
                file.write(new_file)  # updates the new content

    elif command == 'Delete':
        if file_exists(file_name):
            path = os.path.abspath(file_name)
            os.remove(path)

    line = input()
