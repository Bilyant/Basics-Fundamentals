number = int(input())
searched_word = input()
items = []
filtered_items = []

for i in range(number):
    item = input()
    if searched_word in item:
        filtered_items.append(item)
    items.append(item)

print(items)
print(filtered_items)
