words = input().split()
result = {}

for word in words:
    count = 0
    with open('words.txt') as file:
        for line in file:
            for w in line.split():
                el = ''.join([ch for ch in w if ch.isalpha()])
                if el.lower() == word:
                    count += 1
        result[word] = count

final = dict(sorted(result.items(), key=lambda x: -x[1]))

with open('output.txt', 'w') as file:
    for k, v in final.items():
        file.writelines(f'{k} - {v}\n')
