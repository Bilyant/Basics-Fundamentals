number = int(input())
usernames = set()

for _ in range(number):
    usernames.add(input())

print(*usernames, sep='\n')
