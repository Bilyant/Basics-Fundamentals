import os

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')

# try:
#     os.path.exists('my_first_file.txt')
#     os.remove('my_first_file.txt')
# except FileNotFoundError:
#     print('File already deleted!')
