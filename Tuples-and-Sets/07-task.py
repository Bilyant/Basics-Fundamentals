n, m = [int(x) for x in input().split()]  # lengths of two separate sets
lines = n + m
set_n = set()
set_m = set()

for i in range(lines):
    number = input()
    if i < n:
        set_n.add(number)
    else:
        set_m.add(number)

intersection = set_n.intersection(set_m)
print(*intersection, sep='\n')
