def create_chars_in_range(char_1, char_2):
    result = []
    for i in range(ord(char_1) + 1, ord(char_2)):
        result.append(chr(i))
    return ' '.join(result)

first_char = input()
second_char = input()
print(create_chars_in_range(first_char, second_char))
