number_int = list(map(int, input()))
max_number = list()
for digit in range(len(number_int)):
    max_num = max(number_int)
    max_number.append(str(max_num))
    number_int.remove(max_num)
print("".join(max_number))
