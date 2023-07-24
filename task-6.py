current_year = int(input())
next_happy_year = False
while not next_happy_year:
    current_year += 1
    set_year = set(str(current_year))
    next_happy_year = len(str(current_year)) == len(set_year)
print(current_year)
