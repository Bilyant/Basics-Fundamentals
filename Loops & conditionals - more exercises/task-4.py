number = int(input())
all_even = True
for i in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        continue
    print(f"{current_number} is odd!")
    all_even = False
    break
if all_even:
    print("All numbers are even.")
