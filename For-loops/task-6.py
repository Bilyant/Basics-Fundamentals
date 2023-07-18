# a = 1
# e = 2
# i = 3
# o = 4
# u = 5
sum = 0
text = input()
for i in range(0, len(text)):
    if text[i] == "a":
        sum += 1
    elif text[i] == "e":
        sum += 2
    elif text[i] == "i":
        sum += 3
    elif text[i] == "o":
        sum += 4
    elif text[i] == "u":
        sum += 5
print(sum)
