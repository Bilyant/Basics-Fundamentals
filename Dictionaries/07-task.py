number = int(input())
synonims = {}

for i in range(number):
    word = input()
    next_word = input()
    if word not in synonims:
        synonims[word] = []
    synonims[word].append(next_word)

for key, value in synonims.items():
    print(f'{key} - {", ".join(value)}')
