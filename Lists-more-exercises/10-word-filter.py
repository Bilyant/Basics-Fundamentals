data = input().split()
even_words = list(filter(lambda w: len(w) % 2 == 0, data))
print('\n'.join(even_words))
