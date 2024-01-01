"""
Write a program that prints part of the ASCII table characters on the console
separated by a single space.
On the first line of input, you will receive the char index you should start with.
On the second line - the index of the last character you should print.
"""

beginning_num = int(input())
end_num = int(input())
characters = ''

for char_num in range(beginning_num, end_num + 1):
    characters += chr(char_num)

print(' '.join(characters))
