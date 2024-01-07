text = input()
stop_command = 'end'

while text != stop_command:
    # reversed_word = ''.join(list(reversed(text)))
    reversed_word = text[::-1]
    print(f'{text} = {reversed_word}')
    text = input()
