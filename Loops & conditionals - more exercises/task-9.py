text = input()
capital_numbers = list()
for index in range(len(text)):
    if text[index].isupper():
        capital_numbers.append(index)
print(capital_numbers)
