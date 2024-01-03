def palindrome_validator(numbers):
    result = []
    for num in numbers:
        is_Palindrome = False
        current_num = [int(x) for x in str(num)]
        reversed_num = list(reversed(current_num))
        result.append(True) if current_num == reversed_num else result.append(False)
    return '\n'.join([str(x) for x in result])


numbers = [int(x) for x in input().split(', ')]
print(palindrome_validator(numbers))
