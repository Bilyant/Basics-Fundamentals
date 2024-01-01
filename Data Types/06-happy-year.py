current_year = int(input())
is_not_happy_year = True
possible_happy_year = current_year + 1

while is_not_happy_year is True:
    distinct_digits = ''
    for i in range(len(str(possible_happy_year))):
        last_digit = str(possible_happy_year)[i]
        if last_digit not in distinct_digits:
            distinct_digits += last_digit

    if distinct_digits == str(possible_happy_year):
        is_not_happy_year = False
        print(possible_happy_year)
        break

    possible_happy_year += 1
