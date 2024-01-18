def filter_negatives(numbers):
    # return [x for x in numbers if x < 0]
    return list(filter(lambda n: n < 0, numbers))


def filter_positives(numbers):
    # return [x for x in numbers if x >= 0]
    return list(filter(lambda n: n > 0, numbers))


data = [int(x) for x in input().split()]
negatives = sum(filter_negatives(data))
positives = sum(filter_positives(data))
print(negatives)
print(positives)
if abs(negatives) > abs(positives):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
