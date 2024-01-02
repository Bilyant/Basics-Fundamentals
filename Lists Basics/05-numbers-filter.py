num = int(input())
numbers = []
filtered_numbers = []

even = []
odd = []
positive = []
negative = []

for _ in range(num):
    current_num = int(input())
    if current_num % 2 == 0:
        even.append(current_num)
    else:
        odd.append(current_num)
    if current_num >= 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

filter_word = input()
print(eval(filter_word))

# if filter_word == 'even':
#     print(even_numbers)
# elif filter_word == 'odd':
#     print(odd_numbers)
# elif filter_word == 'positive':
#     print(positive_numbers)
# elif filter_word == 'negative':
#     print(negative_numbers)
