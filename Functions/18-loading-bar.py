def create_loading_bar(number):
    percents = (number // 10)
    dots = 10 - percents
    if percents < 10:
        result = [
            f'{number}% [{percents * "%"}{dots * "."}]',
            'Still loading...'
        ]
    else:
        result = [
            f'{number}% Complete!',
            f'[{percents * "%"}]',
        ]
    return '\n'.join(result)


number = int(input())
print(create_loading_bar(number))
