def check_if_contains(first_seq, second_seq):
    result = []
    for item in first_seq:
        for second_item in second_seq:
            if item in second_item:
                if item not in result:
                    result.append(item)
    return result


first_sequence = input().split(', ')
second_sequence = input().split(', ')
result = check_if_contains(first_sequence, second_sequence)
print(result)
