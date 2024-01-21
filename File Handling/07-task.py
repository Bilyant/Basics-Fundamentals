result = []

with open('words.txt') as file:
    for idx, line in enumerate(file):
        letters_count = 0
        others_count = 0
        for word in line.split():
            for ch in word:
                if ch.isalpha():
                    letters_count += 1
                else:
                    others_count += 1
        result.append(f'Line {idx+1}: {line} ({letters_count})({others_count})')

with open('output.txt', 'w') as file:
    file.write('\n'.join(result))
