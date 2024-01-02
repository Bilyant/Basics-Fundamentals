cards = input().split(' ')
num = int(input())
shuffled_deck = []

for i in range(2):
    for y in range(i, len(cards), 2):
        if i % 2 == 0:
            shuffled_deck.append(cards[y])
        else:
            shuffled_deck.append(cards[y])

print(shuffled_deck)
