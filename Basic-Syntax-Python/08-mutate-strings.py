first_string = input()
second_string = input()
result = ''

for i in range(len(first_string)):
    new_word = second_string[:i+1] + first_string[i+1:]
    if new_word != result:
        result = new_word
        print(new_word)
