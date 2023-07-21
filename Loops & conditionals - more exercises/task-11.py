special_words = ["sand", "water", "fish", "sun"]
text = input().lower()
counter = 0
for word in special_words:
    while word in text:
        counter += 1
        text = text.replace(word, "", 1)
print(counter)
