def check_if_perfect(number):
    divisors = []
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
    if sum(divisors) == number:
        return 'We have a perfect number!'
    else:
        return "It's not so perfect."


number = int(input())
print(check_if_perfect(number))
