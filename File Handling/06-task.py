symbols = {"-", ",", ".", "!", "?"}
result = []


def replace_chars(text: str):
    for symbol in symbols:
        if symbol in text:
            text = text.replace(symbol, '@')
    return text


with open('words.txt') as file:
    for idx, line in enumerate(file):
        new_line = []
        if idx % 2 == 0:
            for word in line.split():
                new_word = replace_chars(word)
                new_line.append(new_word)
            result.append(' '.join(reversed(new_line)))

print('\n'.join(result))
