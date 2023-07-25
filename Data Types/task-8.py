number = int(input())
is_prime = False
if number > 1:
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
        else:
            is_prime = True
if not is_prime:
    print("False")
else:
    print("True")
    